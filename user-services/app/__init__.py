from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
api = Api()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config.from_object('config')

db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    login = db.Column(db.String(100),unique=True,nullable = True)
    password = db.Column(db.String(500),nullable = True)
    isAdmin = db.Column(db.Boolean,default = False)
    dickSize = db.Column(db.Integer,default = False)

db.create_all()

from app import routes