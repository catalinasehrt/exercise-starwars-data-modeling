import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Apellidos = Column(String(250))    
    Contraseña=Column(String(20)) 
    Edad = Column (String(2))
    Email= Column(String(250))

class Personajes(Base):
    __tablename__= 'Personajes'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Genero = Column(String(100))
    Especie = Column(String(250))
   
  
   

class Planetas (Base):
    __tablename__='Planetas'
    id = Column(Integer, primary_key=True)
    Nombre = Column(String(250))
    Poblacion = Column(String(250))
    Clima = Column(String(300))
    Especies = Column(String(250))
    
   
    
    
 
class Personajes_favoritos (Base):    
    __tablename__ = 'Personajes_favoritos'
    id = Column(Integer, primary_key=True)
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    Personajes_id = Column(Integer, ForeignKey('Personajes.id'))
    relacion_Personajes = relationship('Personajes')
    relacion_Usuario = relationship ('Usuario')

    


class Planetas_favoritos(Base):
    __tablename__='Planetas_favoritos'
    id = Column(Integer, primary_key=True)
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    Planetas_id = Column(Integer, ForeignKey('Planetas.id'))
    relacion_Planetas = relationship('Planetas')
    relacion_Usuario = relationship ('Usuario')





# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define Columns for the table person
#     # Notice that each Column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define Columns for the table address.
#     # Notice that each Column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
