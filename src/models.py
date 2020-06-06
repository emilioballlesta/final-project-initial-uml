import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String(10), nullable=False)
    lastname = Column(String(10), nullable=False)
    email = Column(String(10), nullable=False)
    password = Column(String(6), nullable=False)
    login_function = Column(String(6))
    register_function = Column(String(6))
    forgot_my_password_function = Column(String(6))

class Petition(Base):
    __tablename__ = 'Petition'
    id = Column(Integer, primary_key=True)
    description = Column(String()) 

class Order(Base):
    __tablename__ = 'Order'
    id = Column(Integer, primary_key=True)
    consumer_name = Column(String(10), nullable=False) 
    consumer_lastname = Column(String(10), nullable=False) 
    consumer_email = Column(String(), nullable=False) 
    city = Column(String(10), nullable=False)
    state = Column(String(10), nullable=False)
    courrier = Column(String(10), nullable=False)
    postCode = Column(Integer, nullable=False)
    petition_id = Column(Integer, ForeignKey('Petition.id'))
    petition = relationship(Petition)

class Consumer(Base): #cliente
    __tablename__ = 'Consumer'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    petition_id = Column(Integer, ForeignKey('Petition.id'))
    petition = relationship(Petition)

class Entrepreneur(Base): #emprendedor
    __tablename__ = 'Entrepreneur'
    id = Column(Integer, primary_key=True)
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)
    order_id = Column(Integer, ForeignKey('Order.id'))
    order = relationship(Order)

class Billing_details(Base):
    __tablename__ = 'Billing details'
    id = Column(Integer, primary_key=True)
    cardNumber = Column(Integer, nullable=False)
    cvv = Column(Integer, nullable=False)
    expiration_date = Column(String(), nullable=False)
    entrepreneur_id = Column(Integer, ForeignKey('Entrepreneur.id'))
    entrepreneur = relationship(Entrepreneur)

class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(Integer, nullable=False)
    selected = Column(String()) #en realidad es boolean, pero no lo puedo indicar con este template.
    description = Column(String())
    petition_id = Column(Integer, ForeignKey('Petition.id'))
    petition = relationship(Petition)

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')