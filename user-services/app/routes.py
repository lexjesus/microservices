from requests import request
from . import User, app
from . import api
from . import db
import json
from flask import Flask, jsonify, redirect
from flask_restful import Api, Resource, reqparse
from collections import OrderedDict

parser = reqparse.RequestParser()
parser.add_argument("login", type=str)
parser.add_argument("password", type=str)
parser.add_argument("dickSize", type=int)

class Main(Resource):
    def get(self):
        users = User.query.all()
        employee = []
        content = {}
        for user in users:
            content = {'login':user.login,'password':user.password, 'dickSize':user.dickSize}
            employee.append(content)
            content = {}
        return jsonify(employee)
    
    def put(self):
        checklogin = parser.parse_args()["login"]
        checkpassword = parser.parse_args()["password"]
        userModel = User(login = checklogin,password = checkpassword)
        curuser = User.query.filter_by(login=checklogin,password = checkpassword).first()
        print({'login':curuser.login,'isAdmin':curuser.isAdmin})
        return {'login':curuser.login,'isAdmin':curuser.isAdmin}


    def post(self):
        newlogin = parser.parse_args()["login"]
        newpassword = parser.parse_args()["password"]
        newDickSize = parser.parse_args()["dickSize"]
        userModel = User(login = newlogin,password = newpassword, dickSize = newDickSize)
        try:
            db.session.add(userModel)
            db.session.commit()
            return True
        except:
            return "Error!"

    

api.add_resource(Main, "/api/users")
api.init_app(app)
