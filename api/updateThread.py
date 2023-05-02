from confLoader import ConfLoader
import asyncio
import time
from threading import Thread
from console import Console
import pandas

class Station:
    def __init__(self) -> None:
        pass

class UpdateQueue:
    def __init__(self,config: ConfLoader,stationList: list):
        self.timeout = config.timeout
        self.url = config.url
        self.stationList = stationList
     
    def updateQueue(self):
        while True:
            print(Console.warning("Updating stations"))
            result = pandas.read_json(self.url,convert_dates=True)
            indexed = False
            for station in result['datos']:
                #Check if the station with the code is alredy indexed or it must be created
                for i in range(len(self.stationList)):
                    if self.stationList[i]["stationCode"] == station['codigo']: #If is indexed, we update the values of the station
                        self.stationList[i]({
                        "stationCode": station['codigo'],
                        "codeUrl": station['urlIcono'],
                        "porcentage": station['porcentajeNivel'],
                        "longitude": station['coordenadas'][0]['latitud'],
                        "latitude": station['coordenadas'][0]['longitud']
                        })
                        indexed = True    
                if not indexed: #If isn't indexed we append a new dictionary and then add the values
                    self.stationList.append({
                        "stationCode": station['codigo'],
                        "codeUrl": station['urlIcono'],
                        "porcentage": station['porcentajeNivel'],
                        "longitude": station['coordenadas'][0]['latitud'],
                        "latitude": station['coordenadas'][0]['longitud']
                    })
                #print(f"Station code: {station['codigo']}\ncodeUrl: {station['urlIcono']}\nporcentage: {station['porcentajeNivel']}\nlongitude{station['coordenadas'][0]['latitud']}\nlatitude: {station['coordenadas'][0]['longitud']}")
            print(Console.info("Updated successfully"))
            time.sleep(self.timeout) #sleep until next update
       
    def run(self):
            process = Thread(target=self.updateQueue)
            process.start()
            print(Console.info("updateQueueThread initialized successfully"))
        