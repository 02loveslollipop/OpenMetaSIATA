import requests
from console import Console
from apiRequest import ApiRequest
from confLoader import ConfLoader
from flask import Flask, render_template, session, redirect, request, url_for
#from flask_session import Session
from functools import wraps

SESSION_TYPE = 'memcache'
web = Flask(__name__, static_url_path='/static')
#sess = Session()

authorization = "MY_SECRET_TOKEN"

passwordRequest = ApiRequest(host="127.0.0.1",port='6969',argsList=["Authorization","Hash","User"])

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        if 'username' not in session:
            return redirect(url_for('login'))
        return func(*args, **kwargs)
    return wrapper

def checkPasswordRequest(request: requests.Response) -> bool:
    try:
        print(request.json()['response'])
        return eval(request.json()['response'])
    except requests.exceptions.JSONDecodeError:
        print(Console.warning("An error occurred trying to decode the JSON response from the API, the log will be take as False"))
        return False

@web.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if checkPasswordRequest(passwordRequest.request([authorization,password,username])):
            session['username'] = username
            return redirect(url_for('map'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@web.route('/')
@login_required
def map():
    username = session['username']
    return render_template('map.html', username=username)

# Define the logout route
@web.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    web.secret_key = 'MY_SECOND_SECRET_KEY'
    web.config['SESSION_TYPE'] = 'memcached'
    web.run(debug=True)