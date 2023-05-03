from flask import Flask, request, jsonify
from confLoader import ConfLoader
from database import DataBase

app = Flask(__name__)

config = ConfLoader() #The class load the config of config.yml
database = DataBase(type='csv',path='./users.csv')

# The route in this case CheckLevel, and the index as part of the route, the token is pass in the header of the GET request
@app.route('/<password>', methods=['GET'])
def get_value(password):
    return database.get(), 200

@app.route('/list', methods=['GET'])
def get_list():
    return database.get(), 200

#Check that is running in the main
if __name__ == '__main__':
    app.run(debug=config.debug,host=config.host,port=config.port) #Start Flask using the configuration of config.yml