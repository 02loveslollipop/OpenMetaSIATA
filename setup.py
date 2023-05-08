import yaml
import os
import secrets

def guidedSetup() -> None:
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
    print("Please enter the timeout value in second, this value it's the time in seconds between evert time the API request updated data of the stations:")
    while not option:
        selection = input()
        try:
            option = True
            timeout = int(selection)
        except ValueError:
            clear()
            print('the value entered value is not valid as a timeout, please enter a valid value:')   
    
    clear()
    option = False
    print("Please enter the token you want to use for the API, if you enter a void value a random 32 bytes hash will be generated:")
    while not option:
        selection = input()
        if len(selection) == 0:
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
            dbToken = secrets.token_urlsafe(32)
        else:
            option = True
            dbToken = selection
            
        
    clear()
    option = False
    print("Please enter the database or file type you want to use for the users:\n1.CSV (default)\n2.Excel\n3.Access\n4.PostgreSQL\n5.mySQL\n6.MicrosoftSQL\n7.custom")
    while not option:
        if selection == '1':
            type = "csv"
        elif selection == '2':
            type = "excel"
        elif selection == '3':
            type = "access"
        elif selection == '4':
            type = "postgresql"
        elif selection == '5':
            type = "mysql"
        elif selection == '6':
            type = "mssql"
            
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
    

            
    
    
    with open("data.yaml") as f:
        list_doc = yaml.safe_load(f)

    for sense in list_doc:
        if sense["name"] == "sense2":
            sense["value"] = 1234

    with open("data.yaml", "w") as f:
        yaml.dump(list_doc, f)

def advanceSetup() -> None:
    clear()
    print('The advance setup allow to make a custom installation either because you alredy have a config file for the API,DB and WEB, or because you want to modify manually the YAML files. This script will build the docker containers and will execute them.\nPress any button to start...')
    input()
    os.system('bash setup.sh')

def updateContainser() -> None:
    clear()
    print('The update allow to make any modification to the source files of the containers either because you changed the configurations or because you changed any other file such as photos, users, etc.\nPress any button to start...')
    input()
    os.system('bash update.sh')
    
def clear() -> None:
    os.system('clear')

option = False
print('Welcome to the OpenMetaSIATA setup assistant, please select one of the setup options:\n1.Guided setup (easy method)\n2.Advance setup\n3.Update containers')
while not option:
    selection = input()
    if selection == '1':
        pass
    elif selection == '2':
        pass
    elif selection == '3':
        pass
    else:
        clear()
        print('The selection is invalid, please select a valid option:\n1.Guided setup (easy method)\n2.Advance setup\n3.Update containers')



