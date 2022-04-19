from logging import log
from sqlalchemy import null
from . import app
from flask import Flask,render_template, url_for, request,session, redirect,flash
import requests

menu = [{"name": "Home page", "url":"/ui-services/index"},
        {"name": "Registration", "url":"/ui-services/registr"},
        {"name": "Log in", "url":"/ui-services/login"},
        {"name": "Exit", "url":"/ui-services/exit"},
        {"name": "Users", "url":"/ui-services/viewusers"},
        {"name": "Items", "url":"/ui-services/viewproduct"}]

    
urlUsers = "http://user-services:5001/api/users"
urlProducts = "http://product-services:5002/api/product"

@app.route('/')
@app.route('/ui-services/index')
def index():
    if 'login' in session:
        return render_template("index.html", menu = menu,   ses = session['login'])
    else:
        return render_template("index.html", menu = menu,   ses = 'nonSession')

@app.route('/ui-services/exit')
def exit():
    session.pop('login',None)
    session.pop('isAdmin',None)
    return redirect(url_for('index'))

@app.route('/ui-services/login', methods=["POST","GET"])
def login():
    if request.method == 'POST':
        res = requests.put(urlUsers,json = {'login':request.form["login"],"password":request.form["password"]})
        if res.json():
            print(res.json())
            session['login'] = res.json()['login']
            session['isAdmin'] = res.json()['isAdmin']
            return redirect(url_for('index'))
        else:
            flash('Polupoker not found')

    return render_template("login.html", menu = menu)

@app.route('/ui-services/registr', methods=["POST","GET"])
def registr():
    if request.method == 'POST':
        res = requests.post(urlUsers, json = {'login':request.form["login"],"password":request.form["password"], "dickSize": request.form["dickSize"]})
    return render_template("registr.html", menu = menu)

@app.route('/ui-services/viewusers')
def viewusers():
    if session.get('isAdmin') == True:
        res = requests.get(urlUsers)
        return render_template("viewUsers.html", menu = menu,viewusers = res.json())
    else:
        return render_template("viewUsers.html", menu = menu, error = "Access denied!")

@app.route('/ui-services/viewproduct')
def viewproduct():
    res = requests.get(urlProducts)
    if 'isAdmin' in session: 
        return render_template("viewproduct.html", menu = menu,viewproduct = res.json(),isAdmin = session['isAdmin'])
    else:
        return render_template("viewproduct.html", menu = menu,viewproduct = res.json(),isAdmin = False)

@app.route('/ui-services/createproduct', methods=["POST","GET"])
def createproduct():
    if request.method == 'POST':
        res = requests.post(urlProducts, json = {'name':request.form["name"],"price":request.form["price"]})
    return redirect(url_for('viewproduct'))

@app.route('/ui-services/deleteproduct', methods=["POST","GET"])
def deleteproduct():
    if request.method == 'POST':
        res = requests.delete(urlProducts, json = {'name':request.form["name"]})
    return redirect(url_for('viewproduct'))
    