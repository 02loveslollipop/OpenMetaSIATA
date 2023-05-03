import requests
from console import Console

class ApiRequest:
    def __init__(self, host: str, argsList: list, port: str = 80,resource: str = None, protocol: str = 'http') -> None:
        self.host = host
        self.port = port
        self.port = port
        self.resource = resource
        self.protocol = protocol
        self.argsList = argsList
        if self.resource == None:
            self.url = f"{self.protocol}://{self.host}:{self.port}/"
        else:    
            self.url = f"{self.protocol}://{self.host}:{self.port}/{resource}/"
        
    def request(self,args: list) -> requests.Response:
        
        if len(args) != len(self.argsList):
            raise ValueError("The length of the args and the argsList is different")

        header = {}
        for i in range(len(args)):
            header.update({self.argsList[i]: args[i]})
            
        print(header) #TODO: quitar esto
        
        return requests.get(self.url, headers=header)