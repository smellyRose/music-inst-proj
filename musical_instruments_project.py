from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, User, MusicalInstrument, Model

from flask import session as login_session
import random
import string

from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2
import json
from flask import make_response
import requests

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Musical Instrument Application"


# Connect to Database and create database session
try:
    engine = create_engine('sqlite:///instrumentmodels.db')
    Base.metadata.bind = engine
except BaseException:
    print ("Unable to connect to the database")

DBSession = sessionmaker(bind=engine)
session = DBSession()

allAvailableColors = [
    'Red',
    'White',
    'Black',
    'Sunburst',
    'Blue',
    'Green',
    'Natural',
    'Blue Sparkle',
    'Red Sparkle',
    'Brass',
    'Gold']


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code
    code = request.data

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        print "Token's client ID does not match app's."
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(
            json.dumps('Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    login_session['access_token'] = credentials.access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': credentials.access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h1>Welcome, '
    output += login_session['username']
    output += '!</h1>'
    output += '<img src="'
    output += login_session['picture']
    output += """ " style = "width: 300px; height: 300px;border-radius: 150px;
            -webkit-border-radius: 150px;-moz-border-radius: 150px;"> """
    flash("you are now logged in as %s" % login_session['username'])
    return output


# User Helper Functions
def createUser(login_session):
    newUser = User(name=login_session['username'], email=login_session[
                   'email'], picture=login_session['picture'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserID(email):
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except BaseException:
        return None


# DISCONNECT - Revoke a current user's token and reset their login_session
@app.route('/gdisconnect')
def gdisconnect():
    # Only disconnect a connected user.
    access_token = login_session.get('access_token')
    if access_token is None:
        response = make_response(
            json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]

    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        return render_template('logoutsuccess.html')
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(
            json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# JSON API to view Instrument  Information
@app.route('/instrument/<int:instrument_id>/model/JSON')
def instrumentModelJSON(instrument_id):
    if 'username' not in login_session:
        return redirect('/login')
    models = session.query(Model).filter_by(
        musicalInstrument_id=instrument_id).all()
    return jsonify(Model=[i.serialize for i in models])


@app.route('/instrument/<int:instrument_id>/model/<int:model_id>/JSON')
def modelJSON(instrument_id, model_id):
    if 'username' not in login_session:
        return redirect('/login')
    model = session.query(Model).filter_by(
        musicalInstrument_id=instrument_id).filter_by(
        id=model_id).one()
    return jsonify(Model=model.serialize)


@app.route('/instrument/JSON')
def instrumentsJSON():
    instruments = session.query(MusicalInstrument).all()
    return jsonify(instruments=[r.serialize for r in instruments])


# Show all instruments
@app.route('/')
@app.route('/instrument/')
def showInstruments():
    musicalInstruments = session.query(
        MusicalInstrument).order_by(asc(MusicalInstrument.id))
    if 'username' not in login_session:
        return render_template(
            'publicinstruments.html',
            musicalInstruments=musicalInstruments)
    else:
        return render_template(
            'instruments.html',
            musicalInstruments=musicalInstruments)


# Create a new instrument
@app.route('/instrument/new/', methods=['GET', 'POST'])
def newInstrument():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        selectedColors = request.form.getlist('selectedColor')
        formattedColors = ''
        for i in range(len(selectedColors)):
            formattedColors += selectedColors[i]
            if i < len(selectedColors) - 1:
                formattedColors += ','
        newInstrument = MusicalInstrument(
            name=request.form['name'],
            user_id=login_session['user_id'],
            availableColors=formattedColors)
        session.add(newInstrument)
        flash('New Instrument %s Successfully Created' % newInstrument.name)
        session.commit()
        return redirect(url_for('showInstruments'))
    else:
        return render_template(
            'newInstrument.html',
            availableColors=allAvailableColors)


# Edit a musical instrument
@app.route('/instrument/<int:instrument_id>/edit/', methods=['GET', 'POST'])
def editMusicalInstrument(instrument_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedInstrument = session.query(
        MusicalInstrument).filter_by(id=instrument_id).one()
    if login_session['user_id'] != editedInstrument.user_id:
        return render_template('useridmismatch.html')
    if request.method == 'POST':
        if request.form['name']:
            editedInstrument.name = request.form['name']
            flash('Instrument Successfully Edited %s' % editedInstrument.name)
            return redirect(url_for('showInstruments'))
    else:
        return render_template(
            'editInstrument.html',
            instrument=editedInstrument)


# Delete an instrument
@app.route('/instrument/<int:instrument_id>/delete/', methods=['GET', 'POST'])
def deleteInstrument(instrument_id):
    if 'username' not in login_session:
        return redirect('/login')
    instrumentToDelete = session.query(
        MusicalInstrument).filter_by(id=instrument_id).one()
    if login_session['user_id'] != instrumentToDelete.user_id:
        return render_template('useridmismatch.html')
    if request.method == 'POST':
        session.delete(instrumentToDelete)
        flash('%s Successfully Deleted' % instrumentToDelete.name)
        session.commit()
        return redirect(
            url_for(
                'showInstruments',
                instrument_id=instrument_id))
    else:
        return render_template(
            'deleteInstrument.html',
            instrument=instrumentToDelete)


# Show an instrument model
@app.route('/instrument/<int:instrument_id>/')
@app.route('/instrument/<int:instrument_id>/model/')
def showModels(instrument_id):
    instrument = session.query(
        MusicalInstrument).filter_by(id=instrument_id).one()
    models = session.query(Model).filter_by(
        musicalInstrument_id=instrument_id).all()
    if 'username' not in login_session:
        loggedInStatus = False
    else:
        loggedInStatus = True
    return render_template(
        'models.html',
        models=models,
        instrument=instrument,
        loggedInStatus=loggedInStatus)


# Create a new model
@app.route(
    '/instrument/<int:instrument_id>/model/new/',
    methods=[
        'GET',
        'POST'])
def newModel(instrument_id):
    if 'username' not in login_session:
        return redirect('/login')
    instrument = session.query(
        MusicalInstrument).filter_by(id=instrument_id).one()
    if request.method == 'POST':
        selectedColor = request.form.getlist('selectedColor')
        newModel = Model(
            name=request.form['name'],
            description=request.form['description'],
            price=request.form['price'],
            color=selectedColor[0],
            musicalInstrument_id=instrument_id,
            user_id=login_session['user_id'])
        session.add(newModel)
        session.commit()
        flash('New Model %s Successfully Created' % (newModel.name))
        return redirect(url_for('showInstruments'))
    else:
        availableColors = instrument.availableColors.split(',')
        return render_template(
            'newModel.html',
            instrument=instrument,
            availableColors=availableColors)


# Edit model
@app.route(
    '/instrument/<int:instrument_id>/model/<int:model_id>/edit',
    methods=[
        'GET',
        'POST'])
def editModel(instrument_id, model_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedModel = session.query(Model).filter_by(id=model_id).one()
    if login_session['user_id'] != editedModel.user_id:
        return render_template('useridmismatch.html')
    instrument = session.query(MusicalInstrument).filter_by(
        id=instrument_id).one()
    availableColors = instrument.availableColors.split(',')
    if request.method == 'POST':
        if request.form['name']:
            editedModel.name = request.form['name']
        if request.form['description']:
            editedModel.description = request.form['description']
        if request.form['price']:
            editedModel.price = request.form['price']
        if request.form['color']:
            editedModel.color = request.form['color']
        session.add(editedModel)
        session.commit()
        flash('Model Successfully Edited')
        return redirect(url_for('showModels', instrument_id=instrument_id))
    else:
        return render_template(
            'editmodel.html',
            instrument_id=instrument_id,
            model_id=model_id,
            model=editedModel,
            availableColors=availableColors)


# Delete a model
@app.route(
    '/instrument/<int:instrument_id>/model/<int:model_id>/delete',
    methods=[
        'GET',
        'POST'])
def deleteModel(instrument_id, model_id):
    if 'username' not in login_session:
        return redirect('/login')
    instrument = session.query(MusicalInstrument).filter_by(
        id=instrument_id).one()
    modelToDelete = session.query(Model).filter_by(id=model_id).one()
    if login_session['user_id'] != modelToDelete.user_id:
        return render_template('useridmismatch.html')
    if request.method == 'POST':
        session.delete(modelToDelete)
        session.commit()
        flash('Model Successfully Deleted')
        return redirect(url_for('showModels', instrument_id=instrument_id))
    else:
        return render_template(
            'deleteModel.html',
            instrument_id=instrument_id,
            model=modelToDelete)


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000, threaded=False)
