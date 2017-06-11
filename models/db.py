'''
  this file includes initial setup for project.
'''

from flask import Flask, render_template, request, redirect
from flask import jsonify, url_for, flash
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, News, User

from flask import session as login_session

# used to create a pseduo-random string that will identify each session
import random
import string


# for creating flow object
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
import httplib2

# helps in converting in-memory python objects to a searilised
# representation known as JSON
import json
from flask import make_response


# apache2 licensed http lib similar to urllib but with a few improvements
import requests

# SeaSurf is a Flask Extension for preventing cross-site request forgery
from flask.ext.seasurf import SeaSurf

app = Flask(__name__)

CLIENT_ID = json.loads(
    open('client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "News Catalogue Application"

# Protecting the app against CSRF attacks.
csrf = SeaSurf(app)

# Connect to Database and create database session
engine = create_engine('sqlite:///newswebapplication.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()
