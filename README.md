# Musical Instrument Project
This web application manages and displays musical instruments and models stored within a database. Logging in through Google will validate that user. Valid users have the ability to create new instruments, edit instrument names, and delete instruments. Within an individual instrument classification, valid users can add, edit and delete models.

If a logged in user attempts to edit or delete an instrument that they did not create, they will be redirected to a page that warns them that they are not authorized to modify this instrument.

Similarly to instruments, logged in users cannot edit or delete models they did not create. A logged in user can add a model to an instrument they did not create, and take ownership of that model so other users cannot modify that model.

Users that are not logged in can only read the instrument list and the list of models contained within each instrument. 

If an instrument or model is edited, that instrument or model will be updated within the database. Similarly, if an instrument or model is deleted, that instrument or model will be removed from the database.

JSON endpoints are only accessible to users that have successfully logged in. If a user is not logged in, the instrument list will not display the option to view the JSON and will be redirected to the login page if the user requests to view a model’s JSON. Successfully logged in users will be able to view JSONs of any instrument or model. 


## Prerequisites
Access to a operating system capable of installing Vagrant.

## Installing
* Install [VirtualBox 5.1](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
* Install [Vagrant](https://www.vagrantup.com/downloads.html)
* In a terminal navigate to the root directory of vagrant.
* Enter the command `vagrant up`, to boot the Vagrant environment
* Enter the command `vagrant ssh`, to login
* Download the musical instrument project [GitHub Repo](https://github.com/smellyRose/music-inst-proj) and unzip
* Copy the contents of the download into the same directory as the working Vagrant environment
* Navigate to the folder containing the `musical_instruments_project.py` file
* Enter the command `python musical_instruments_project.py` to run the web application

#### Running the web application
* Once the vagrant application is running within the Vagrant environment, visit `localhost:5000` in a browser
* To modify instruments, click on the `Login` link and login with Google. 

#### Built With
Python 2.7

#### Authors
Joey Berger