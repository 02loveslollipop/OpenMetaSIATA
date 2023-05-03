import yaml
from console import Console

class ConfLoader:
    def __init__(self):
    
        try:
            configFile = open('config.yml')
            print(Console.info("Using config.yml"))
        except FileNotFoundError:
            print(Console.warning("You don't have a config.yml file, using example_config.yml"))
            configFile = open('example_config.yml')
        finally:
            try:
                config = yaml.load(configFile, Loader=yaml.FullLoader)
                self.host = config['network']['host']
                self.port = config['network']['port']
                self.debug = config['api']['debug']
                self.token = config['api']['token']
                self.type = config['database']['type']
                self.path = config['database']['path']
                self.database = config['database']['database']
                self.user = config['database']['user']
                self.password = config['database']['password']
                self.dbHost = config['database']['host']
                self.dbPort = config['database']['port']
                self.url = config['database']['url']
                        
            except KeyError as err:
                import traceback
                print(Console.error(str(type(err))))
                print(Console.error(str(err.args)))
                print(Console.error(str(traceback.format_exc())))
                print(Console.warning("Couldn't start due of a bad configuration in confg.yml, please check your confg.yml"))
                exit()