from flask import Flask, request, jsonify
from confLoader import ConfLoader
from database import DataBase

app = Flask(__name__)

config = ConfLoader() #The class load the config of config.yml
database = DataBase(type='csv',path='./users.csv')

# The route in this case CheckLevel, and the index as part of the route, the token is pass in the header of the GET request
@app.route('/', methods=['GET'])
def get_value():
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'There is no token in this request'}), 401 #HTTP 401 means that is unauthorized, because there is no token
    
    if 'User' not in request.headers:
        return jsonify({'error': 'There is no user in this request'}), 401 #HTTP 401 means that is unauthorized, because there is no user to check
    
    if 'Hash' not in request.headers:
        return jsonify({'error': 'There is no hash in this request'}), 401 #HTTP 401 means that is unauthorized, because there is no hash to check
    
    user = request.headers.get('User') #Retrieve the user as string
    hash  = request.headers.get('Hash') #Retrieve the hash as string
    token = request.headers.get('Authorization') #retrieve the token as an string
    
    #Validadte the token:
    if  not token == config.token: #If the token isn't valid 
        return jsonify({'error': 'The token is not valid, if you think this is an error please contact an administrator'}), 401 #HTTP 401 means that is unauthorized, because the token isn't valid
    
    return database.check(user=user,passwordHash=hash), 200

@app.route('/list', methods=['GET'])
def get_list():
    
    if 'Authorization' not in request.headers:
        return jsonify({'error': 'There is no token in this request'}), 401 #HTTP 401 means that is unauthorized, because there is no token
    
    token = request.headers.get('Authorization') #retrieve the token as an string
    
    #Validadte the token:
    if  not token == config.token: #If the token isn't valid 
        return jsonify({'error': 'The token is not valid, if you think this is an error please contact an administrator'}), 401 #HTTP 401 means that is unauthorized, because the token isn't valid
    
    return database.get(), 200

#Check that is running in the main
if __name__ == '__main__':
    app.run(debug=config.debug,host=config.host,port=config.port) #Start Flask using the configuration of config.yml