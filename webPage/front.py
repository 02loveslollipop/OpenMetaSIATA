import requests
from console import Console
from apiRequest import ApiRequest
from confLoader import ConfLoader
from flask import Flask, render_template, session, redirect, request, url_for
import plotly.graph_objects as go
import plotly
from functools import wraps
from dash import dcc, html, Dash
import json

SESSION_TYPE = 'memcache'

web = Flask(__name__, static_url_path='/static')

app = Dash(__name__,server=web,url_base_pathname='/dash/')

app.layout = html.Div()

authorization = "MY_SECRET_TOKEN"

passwordRequest = ApiRequest(host="127.0.0.1",port='8080',argsList=["Authorization","Hash","User"])

indexRequest = ApiRequest(host="127.0.0.1",port="7000",argsList=["Authorization"],resource="ListStation")

siataRequest = ApiRequest(host="127.0.0.1",port="7000",argsList=["Authorization"])

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

@web.route('/badapple')
def badapple():
    return render_template('badapple.html')

@web.route('/map')
@login_required
def map():
    username = session['username']
    sessionUrl = url_for('logout')
    sessionMessage = f"{session['username']} - Log Out"
    index = int(indexRequest.request([authorization]).json()['index'])
    
    lat = []
    lon = []
    z = []
    
    for i in range(index):
        siataRequest.setUrl(resource=f"CheckLevel/{i}",protocol=siataRequest.protocol,host=siataRequest.host,port=siataRequest.port)
        currentStation = siataRequest.request([authorization]).json()
        print(f"Longitud: {currentStation['latitude']}\nLatitud: {currentStation['longitude']}\n Porcentage: {currentStation['porcentage']}")
        lon.append(currentStation['latitude'])
        lat.append(currentStation['longitude'])
        z.append(currentStation['porcentage'])

    map = go.Figure(go.Densitymapbox(lat=lat,lon=lon,z=z,radius=20, opacity= 0.9, zmin=0, zmax=100)).update_layout(mapbox_style='open-street-map',mapbox_center_lon=-75.5900293,mapbox_center_lat=6.2414662).update_layout(margin={"r": 0,"t": 0,"l": 0, "b": 0})
    graphJSON = json.dumps(map, cls=plotly.utils.PlotlyJSONEncoder)   
    
    return render_template('map.html', username=username,sessionUrl=sessionUrl,sessionMessage=sessionMessage,graphJSON=graphJSON)

@web.route('/')
def index():
    if 'username' in session:
        username = session['username']
        sessionUrl = url_for('logout')
        sessionMessage = f"{session['username']} - Log Out"
    else:
        username = None
        sessionUrl = url_for('login')
        sessionMessage = f"Log In"
    return render_template('index.html', username=username,sessionUrl=sessionUrl,sessionMessage=sessionMessage)

# Define the logout route
@web.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@web.route('/dash')
def dashMap():
    app.layout = html.Div([
    dcc.Graph(figure=map)
    ])
    return app.index()

if __name__ == '__main__':
    web.secret_key = 'MY_SECOND_SECRET_KEY'
    web.config['SESSION_TYPE'] = 'memcached'
    web.run(debug=True,port='80',host='0.0.0.0')