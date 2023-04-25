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
    