'''
import flask as f
import pandas as pd
url = 'http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json'

webCapture = pd.read_json(url,convert_dates=True)
api = f.Flask(__name__)
HighLevel = []

@api.route('/getStationsLevels')
def showStations():
    for station in webCapture:
        if station['porcentajeNivel'] >= 2:
            pass
            #TODO: Realizar la implementacion de contar los porcentajes
    token = f.request.args
    
    return webCapture.to_string()

if __name__ == '__main__':
    api.run(host='0.0.0.0',port=6969)
'''
from flask import Flask, request, jsonify
from confLoader import ConfLoader
from updateThread import UpdateQueue

app = Flask(__name__)

setup = False
if not setup:
    config = ConfLoader() #The class load the config of config.yml
    stationList = []
    thread = UpdateQueue(config=config,stationList=stationList)
    thread.run()
    setup = True

# The route in this case CheckLevel, and the index as part of the route, the token is pass in the header of the GET request
@app.route('/CheckLevel/<int:index>', methods=['GET'])
def get_value(index):
    # Check if the token is present in the request header
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'There is no token in this request'}), 401 #HTTP 401 means that is unauthorized, because there is no token
    
    token = request.headers.get('Authorization') #retrieve the token as an string
    
    #Validadte the token:
    if  not token == config.token: #If the token isn't valid 
        return jsonify({'error': 'The token is not valid, if you think this is an error please contact an administrator'}), 401 #HTTP 401 means that is unauthorized, because the token isn't valid

    # Check if the index is within the range of the list
    
    if index < 0 or index >= len(stationList):
        return jsonify({'error': 'Invalid index, please check the value you are trying to use'}), 400 #HTTP 400 means that the request isn't valid, in this case beacuse is trying to retrieve an station that doesn't exist
    #If non of the returns is called means that the request is valid, so we return the info about the station with that index
    return stationList[index], 200

#Check that is running in the main
if __name__ == '__main__':
    app.run(debug=config.debug,host=config.host,port=config.port) #Start Flask using the configuration of config.yml