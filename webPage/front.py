import requests
from console import Console
from apiRequest import ApiRequest
from confLoader import ConfLoader
from flask import Flask, render_template, session, redirect, request

web = Flask(__name__)

@web.route('/login')
def login():
    return render_template('login.html')

@web.route('/login', methods=['POST'])
def do_login():
    username = request.form['username']
    password = request.form['password']

    # TODO: Check if username and password are valid

    session['logged_in'] = True
    return redirect('/')

@web.route('/')
def home():
    if not session.get('logged_in'):
        return redirect('/login')
    else:
        return "This is the real content of the page"