import yaml
import os
import secrets

def fastSetup() -> None:
    
    webToken = secrets.token_urlsafe(32)
    apiToken = secrets.token_urlsafe(32)
    dbToken = secrets.token_urlsafe(32)
    
    clear()
    option = False
    print('Please enter your MapBox key:')
    while not option:
        selection = input()
        if selection.startswith('pk.ey'):
            option = True
            style = 'dark'
            mapBoxKey = selection
        else:
            clear()
            print('the token you entered is not valid, please enter a valid MapBox token:')
            
    
    
    while True: #Saving api config
        try:
            clear()
            print("Trying to save api config") 
            with open("./api/config.yml") as f:
                api = yaml.safe_load(f)

            api['api']['token'] = apiToken

            with open("./api/config.yml", "w") as f:
                yaml.dump(api, f)
            break    
        except PermissionError:
            print("File is in use, please close it to save the binary and then press enter")
            input()
            clear()
    
    while True: #Saving db config
        try:
            clear()
            print("Trying to save db config") 
            with open("./db/config.yml") as f:
                db = yaml.safe_load(f)

            db['api']['token'] = dbToken


            with open("./db/config.yml", "w") as f:
                yaml.dump(db, f)
            break    
        except PermissionError:
            print("File is in use, please close it to save the binary and then press enter")
            input()
            clear() 
    
    while True: #Saving web config
        try:
            clear()
            print("Trying to save web config") 
            with open("./web/config.yml") as f:
                web = yaml.safe_load(f)
                
            web['web']['secretKey'] = webToken
            web['map']['token'] = mapBoxKey
            web['apiRequest']['token'] = apiToken
            web['passwordRequest']['token'] = dbToken


            with open("./web/config.yml", "w") as f:
                yaml.dump(web, f)
            break    
        except PermissionError:
            print("File is in use, please close it to save the binary and then press enter")
            input()
            clear()
    
def guidedSetup() -> None:
    
    #web
    webToken = ''
    style = ''
    mapBoxKey = ''
    #db
    type = ''
    dbUrl = ''
    user = ''
    password = ''
    host = ''
    port = ''
    table = ''
    path = ''
    dbToken = ''
    #api
    apiToken = ''
    timeout = ''
    url = ''
    
    clear()
    print("Welcome to the guided setup of OpenMetaSIATA,The open-source SIATA Map Viewer.\nRemember that our source code it's available at https://github.com/02loveslollipop/OpenMetaSIATA.\nPress any button to start the configuration of the services...")
    input()
    
    clear()
    option = False
    print('Please enter the url where the service will retrieve the data, it must return a json:')
    while not option:
        selection = input()
        if selection.startswith('http://') or selection.startswith('https://'):
            option = True
            url = selection
        else:
            clear()
            print('the value entered value is not valid as an url, please enter a valid url:')

    clear()
    option = False
    print("Please enter the timeout value in second, this value it's the interval in seconds which evert the API request update the data of the stations:")
    while not option:
        selection = input()
        try:
            timeout = int(selection)
            option = True
        except ValueError:
            clear()
            print('the value entered value is not valid as a timeout, please enter a valid value:')   
    
    clear()
    option = False
    print("Please enter the token you want to use for the API, if you enter a void value a random 32 bytes hash will be generated:")
    while not option:
        selection = input()
        if selection == '':
            option = True
            apiToken = secrets.token_urlsafe(32)
        else:
            option = True
            apiToken = selection
            
    clear()
    option = False
    print("Please enter the token you want to use for the DB, if you enter a void value a random 32 bytes hash will be generated:")
    while not option:
        selection = input()
        if len(selection) == 0:
            option = True
            dbToken = secrets.token_urlsafe(32)
        else:
            option = True
            dbToken = selection
            
        
    clear()
    option = False
    print("Please enter the database or file type you want to use for the users:\n1.CSV (default)\n2.Excel\n3.Access\n4.PostgreSQL\n5.mySQL\n6.MicrosoftSQL\n7.custom")
    while not option:
        selection = input()
        if selection == '1':
            type = "csv"
            clear()
            option = False
            print('Please enter the path of the csv file:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    option = True
                    path = option
                else:
                    clear()
                    print('You entered a void path, please enter a valid path:')
                    
        elif selection == '2':
            type = "excel"
            clear()
            option = False
            print('Please enter the path of the excel file:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    option = True
                    path = option
                else:
                    clear()
                    print('You entered a void path, please enter a valid path:')
            
        elif selection == '3':
            type = "access"
            clear()
            option = False
            print('Please enter the path of the Access database:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    option = True
                    path = option
                else:
                    clear()
                    print('You entered a void path, please enter a valid path:')
            
        elif selection == '4':
            type = "postgresql"
            clear()
            option = False
            print('Please enter the user of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    user = option
                else:
                    clear()
                    print('You entered a void user, please enter a valid user:')

            clear()
            option = False
            print('Please enter the password of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    password = option
                else:
                    clear()
                    print('You entered a void password, please enter a valid password:')
            
            clear()
            option = False
            print('Please enter the host of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    host = option
                else:
                    clear()
                    print('You entered a void host, please enter a valid host:')
            
            clear()
            option = False
            print('Please enter the port of the DB:')
            while not option:
                selection = input()
                try:
                    fooPort = int(selection)
                    if not (fooPort > 65535 or fooPort < 0):
                        port = fooPort
                        option = True
                    else:
                        clear()
                        print('the value entered value is not a valid port, please enter a valid value:')  
                except ValueError:
                    clear()
                    print('the value entered value is not a valid port, please enter a valid value:')
            
            clear()
            option = False
            print('Please enter the table of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    table = option
                else:
                    clear()
                    print('You entered a void table, please enter a valid table:')
            
        elif selection == '5':
            type = "mysql"
            clear()
            option = False
            print('Please enter the user of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    user = option
                else:
                    clear()
                    print('You entered a void user, please enter a valid user:')

            clear()
            option = False
            print('Please enter the password of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    password = option
                else:
                    clear()
                    print('You entered a void password, please enter a valid password:')
            
            clear()
            option = False
            print('Please enter the host of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    host = option
                else:
                    clear()
                    print('You entered a void host, please enter a valid host:')
            
            clear()
            option = False
            print('Please enter the port of the DB:')
            while not option:
                selection = input()
                try:
                    fooPort = int(selection)
                    if not (fooPort > 65535 or fooPort < 0):
                        port = fooPort
                        option = True
                    else:
                        clear()
                        print('the value entered value is not a valid port, please enter a valid value:')  
                except ValueError:
                    clear()
                    print('the value entered value is not a valid port, please enter a valid value:')
            
            clear()
            option = False
            print('Please enter the table of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    table = option
                else:
                    clear()
                    print('You entered a void table, please enter a valid table:')
                    
        elif selection == '6':
            type = "mssql"
            clear()
            option = False
            print('Please enter the user of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    user = option
                else:
                    clear()
                    print('You entered a void user, please enter a valid user:')

            clear()
            option = False
            print('Please enter the password of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    password = option
                else:
                    clear()
                    print('You entered a void password, please enter a valid password:')
            
            clear()
            option = False
            print('Please enter the host of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    host = option
                else:
                    clear()
                    print('You entered a void host, please enter a valid host:')
            
            clear()
            option = False
            print('Please enter the port of the DB:')
            while not option:
                selection = input()
                try:
                    fooPort = int(selection)
                    if not (fooPort > 65535 or fooPort < 0):
                        port = fooPort
                        option = True
                    else:
                        clear()
                        print('the value entered value is not a valid port, please enter a valid value:')  
                except ValueError:
                    clear()
                    print('the value entered value is not a valid port, please enter a valid value:')
            
            clear()
            option = False
            print('Please enter the table of the DB:')
            while not option:
                selection = input()
                if len(selection) > 0:
                    table = option
                else:
                    clear()
                    print('You entered a void table, please enter a valid table:')
                    
        elif selection == '7':
            type = "custom"
            clear()
            option = False
            print('WARNING: custom will allow you to use any other SQLAlchemy supported database, please check compatibility in further updates of the library\n\nPlease enter the url (Example: myDialect+myDriver://user:password@192.168.1.1:69/test):')
            while not option:
                selection = input()
                if len(selection) > 0:
                    dbUrl = option
                else:
                    clear()
                    print('You entered a void URL, please enter a valid URL:')
        else:
            clear()
            print('The selection is invalid, please select a valid option:\n1.CSV (default)\n2.Excel\n3.Access\n4.PostgreSQL\n5.mySQL\n6.MicrosoftSQL\n7.custom')
    
    clear()
    option = False
    print("Please enter the token you want to use for the user management, if you enter a void value a random 32 bytes hash will be generated:")
    while not option:
        selection = input()
        if len(selection) == 0:
            option = True
            webToken = secrets.token_urlsafe(32)
        else:
            option = True
            webToken = selection
    
    option = False
    print('Please select the map type:\n1.Open street map (no token required)\n2.Mapbox dark theme (mapbox token required)\n3.Mapbox custom style (mapbox token required)')
    while not option:
        selection = input()
        if selection == '1':
            style="open-street-map"
            option = True
            
        elif selection == '2':
            clear()
            option = False
            print('Please enter your MapBox key:')
            while not option:
                selection = input()
                if selection.startswith('pk.ey'):
                    option = True
                    style = 'dark'
                    mapBoxKey = selection
                else:
                    clear()
                    print('the token you entered is not valid, please enter a valid MapBox token:')
                                
        elif selection == '3':
            clear()
            option = False
            print('Please enter your MapBox key:')
            while not option:
                selection = input()
                if selection.startswith('pk.ey'):
                    option = True
                    style = 'dark'
                    mapBoxKey = selection
                else:
                    clear()
                    print('the token you entered is not valid, please enter a valid MapBox token:')
            
            clear()
            option = False
            print('Please enter your MapBox style:')
            while not option:
                selection = input()
                if selection.startswith('mapbox://'):
                    option = True
                    style = selection
                else:
                    clear()
                    print('the style you entered is not valid, please enter a valid MapBox style:')
            
        else:
            clear()
            print('The selection is invalid, please select a valid option:\n1.Open street map (no token required)\n2.Mapbox dark theme (mapbox token required)\n3.Mapbox custom style (mapbox token required)')
    
    
    while True: #Saving api config
        try:
            clear()
            print("Trying to save api config") 
            with open("./api/config.yml") as f:
                api = yaml.safe_load(f)

            api['api']['token'] = apiToken
            api['api']['timeout'] = timeout
            api['api']['url'] = url

            with open("./api/config.yml", "w") as f:
                yaml.dump(api, f)
            break    
        except PermissionError:
            print("File is in use, please close it to save the binary and then press enter")
            input()
            clear()
    
    while True: #Saving db config
        try:
            clear()
            print("Trying to save db config") 
            with open("./db/config.yml") as f:
                db = yaml.safe_load(f)
                
            db['database']['type'] = type
            db['database']['url'] = dbUrl
            db['database']['user'] = user
            db['database']['pasword'] = password
            db['database']['host'] = host
            db['database']['port'] = port
            db['database']['database'] = table
            db['database']['path'] = path
            db['api']['token'] = dbToken


            with open("./db/config.yml", "w") as f:
                yaml.dump(db, f)
            break    
        except PermissionError:
            print("File is in use, please close it to save the binary and then press enter")
            input()
            clear() 
    
    while True: #Saving web config
        try:
            clear()
            print("Trying to save web config") 
            with open("./web/config.yml") as f:
                web = yaml.safe_load(f)
                
            web['web']['secretKey'] = webToken
            web['map']['style'] = style
            web['map']['token'] = mapBoxKey
            web['apiRequest']['token'] = apiToken
            web['passwordRequest']['token'] = dbToken


            with open("./web/config.yml", "w") as f:
                yaml.dump(web, f)
            break    
        except PermissionError:
            print("File is in use, please close it to save the binary and then press enter")
            input()
            clear()
    
def advanceSetup() -> None:
    clear()
    print('The advance setup allow to make a custom installation either because you alredy have a config file for the API,DB and WEB, or because you want to modify manually the YAML files. This script will build the docker containers and will execute them.\nPress any button to start...')
    input()
    os.system('bash setup.sh')

def updateContainer() -> None:
    clear()
    print('The update allow to make any modification to the source files of the containers either because you changed the configurations or because you changed any other file such as photos, users, etc.\nPress any button to start...')
    input()
    os.system('bash update.sh')
    
def clear() -> None:
    os.system('clear')

option = False
print('Welcome to the OpenMetaSIATA setup assistant, please select one of the setup options:\n1.Guided setup (easy method)\n2.Fast setup (default values)\n3.Advance setup\n4.Update containers')
while not option:
    selection = input()
    if selection == '1':
        guidedSetup()
    elif selection == '2':
        fastSetup()
    elif selection == '3':
        advanceSetup()
    elif selection == '4':
        updateContainer()
    else:
        clear()
        print('The selection is invalid, please select a valid option:\n1.Guided setup (easy method)\n2.Advance setup\n3.Update containers')



