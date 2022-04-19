from flask import Flask
from flask_restful import Api, Resource, reqparse
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow


app = Flask(__name__)
api = Api()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///product.db'
app.config.from_object('config')

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer,primary_key = True)
    name= db.Column(db.String(100),unique=True,nullable = True)
    price = db.Column(db.Integer,nullable = True)

db.create_all()
from app import routes