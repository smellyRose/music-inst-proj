from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    picture = Column(String(250))
      

class MusicalInstrument(Base):
    __tablename__ = 'musicalInstrument'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    availableColors = Column(String(250), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'id': self.id,
        }


class Model(Base):
    __tablename__ = 'model'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    color = Column(String(250))
    musicalInstrument_id = Column(Integer, ForeignKey('musicalInstrument.id'))
    musicalInstrument = relationship(MusicalInstrument)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'name': self.name,
            'description': self.description,
            'id': self.id,
            'price': self.price,
            'color': self.color,
        }
        

engine = create_engine('sqlite:///instrumentmodels.db')


Base.metadata.create_all(engine)