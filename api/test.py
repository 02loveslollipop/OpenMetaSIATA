import pandas
url = "http://siata.gov.co:8089/estacionesNivel/cf7bb09b4d7d859a2840e22c3f3a9a8039917cc3/?format=json"
result = pandas.read_json(url,convert_dates=True)
stationList = []
indexed = False
for station in result['datos']:
    for i in range(len(stationList)):
        if stationList[i]["stationCode"] == station['codigo']:
            stationList[i]({
            "stationCode": station['codigo'],
            "codeUrl": station['urlIcono'],
            "porcentage": station['porcentajeNivel'],
            "longitude": station['coordenadas'][0]['latitud'],
            "latitude": station['coordenadas'][0]['longitud']
            })
            indexed = True    
    if not indexed:
        stationList.append({
            "stationCode": station['codigo'],
            "codeUrl": station['urlIcono'],
            "porcentage": station['porcentajeNivel'],
            "longitude": station['coordenadas'][0]['latitud'],
            "latitude": station['coordenadas'][0]['longitud']
        })
    print(f"------NEW STATION------\nStation code: {station['codigo']}\ncodeUrl: {station['urlIcono']}\nporcentage: {station['porcentajeNivel']}\nlongitude{station['coordenadas'][0]['latitud']}\nlatitude: {station['coordenadas'][0]['longitud']}")
    
    


