import requests
from console import Console
from apiRequest import ApiRequest
from confLoader import ConfLoader
from flask import Flask, render_template, session, redirect, request, url_for
import flask as fs
import plotly.graph_objects as go
import plotly
import plotly.express as px
from functools import wraps
import json

web = Flask(__name__, static_url_path='/static')

config = ConfLoader()

px.set_mapbox_access_token(config.mapToken)

passwordRequest = ApiRequest(host=config.passwordHost,port=config.passwordToken,argsList=["Authorization","Hash","User"])

indexRequest = ApiRequest(host=config.apiHost,port=config.apiPort,argsList=["Authorization"],resource="ListStation")

siataRequest = ApiRequest(host=config.apiHost,port=config.apiPort,argsList=["Authorization"])

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
        
        if checkPasswordRequest(passwordRequest.request([config.passwordToken,password,username])):
            session['username'] = username
            return redirect(url_for('map'))
        else:
            return render_template('login.html', error='Invalid username or password')
    else:
        return render_template('login.html')

@web.route('/logout')
@login_required
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

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

@web.route('/badapple')
def badapple():
    return render_template('badapple.html')

@web.route('/map')
@login_required
def map():
    username = session['username']
    sessionUrl = url_for('logout')
    sessionMessage = f"{session['username']} - Log Out"
    index = int(indexRequest.request([config.apiToken]).json()['index'])
    
    lat = []
    lon = []
    z = []
    
    for i in range(index):
        siataRequest.setUrl(resource=f"CheckLevel/{i}",protocol=siataRequest.protocol,host=siataRequest.host,port=siataRequest.port)
        currentStation = siataRequest.request([config.apiToken]).json()
        print(f"Longitud: {currentStation['latitude']}\nLatitud: {currentStation['longitude']}\n Porcentage: {currentStation['porcentage']}")
        lon.append(currentStation['latitude'])
        lat.append(currentStation['longitude'])
        z.append(currentStation['porcentage'])

    layout = go.Layout(autosize=True,mapbox= dict(accesstoken=config.mapToken,bearing=10,pitch=60,zoom=13,center= dict(lat=6.241,lon=-75.590),style=config.mapStyle))

    map = go.Figure(go.Densitymapbox(lat=lat,lon=lon,z=z,radius=20, opacity= 0.9, zmin=0, zmax=100),layout=layout).update_layout(margin={"r": 0,"t": 0,"l": 0, "b": 0})
    graphJSON = json.dumps(map, cls=plotly.utils.PlotlyJSONEncoder)   
    
    return render_template('map.html', username=username,sessionUrl=sessionUrl,sessionMessage=sessionMessage,graphJSON=graphJSON)

@web.route('/table')
@login_required
def table():
    username = session['username']
    sessionUrl = url_for('logout')
    sessionMessage = f"{session['username']} - Log Out"
    index = int(indexRequest.request([config.apiToken]).json()['index'])
    
    lat = []
    lon = []
    z = []
    code = []
    htmlBuffer = ""
    for i in range(index):
        siataRequest.setUrl(resource=f"CheckLevel/{i}",protocol=siataRequest.protocol,host=siataRequest.host,port=siataRequest.port)
        currentStation = siataRequest.request([config.apiToken]).json()
        htmlBuffer+=f"<tr>\n<td>\n{round(currentStation['stationCode'],2)}\n</td>\n<td>\n{round(currentStation['porcentage'],2)}\n</td>\n<td>\n{round(currentStation['longitude'],2)}\n</td>\n<td>\n{round(currentStation['latitude'],2)}\n</td>\n</tr>"
    
    html = f"<table>\n<tr>\n<th>\nStation code\n</th>\n<th>\nPorcentage level\n</th>\n<th>\nLongitude\n</th>\n<th>\nLatitude\n</th>\n</tr>\n{htmlBuffer}\n</table>"
            
    return render_template('table.html', username=username,sessionUrl=sessionUrl,sessionMessage=sessionMessage,tableResult=html)
    

if __name__ == '__main__':
    web.secret_key = config.secretKey
    web.config['SESSION_TYPE'] = 'memcached'
    web.run(debug=config.debug,port=config.port,host=config.host)
