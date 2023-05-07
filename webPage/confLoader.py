import yaml
from console import Console

class ConfLoader:
    def __init__(self):
        """
        Create a class that contains all the configuration parameter for a program
        """
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
                self.apiToken = config['apiRequest']['token']
                self.apiHost = config['apiRequest']['host']
                self.apiPort = config['apiRequest']['port']
                self.passwordToken = config['passwordRequest']['token']
                self.passwordHost = config['passwordRequest']['host']
                self.paswwordPort = config['passwordRequest']['port']
                self.mapStyle = config['map']['style']
                self.mapToken = config['map']['token']
                self.debug = config['web']['debug']
                self.secretKey = config['web']['secretKey']
                        
            except KeyError as err:
                import traceback
                print(Console.error(str(type(err))))
                print(Console.error(str(err.args)))
                print(Console.error(str(traceback.format_exc())))
                print(Console.warning("Couldn't start due of a bad configuration in confg.yml, please check your confg.yml"))
                exit()