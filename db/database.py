import pandas as pd
import sqlalchemy as sql
from flask import jsonify, Response
from console import Console

#Data source is users
class DataBase:
    def __init__(self, type: str = 'csv', path: str = './users.csv', database: str = None, user: str = None, password: str = None, host: str = None, port: str = None, url: str = None) -> None:
        
        if type == 'csv':
            self.dataFrame = pd.read_csv(path)
        elif type == 'excel':
            self.dataFrame = pd.read_excel(path)
        elif type == 'access':
            engine = sql.create_engine(f"access+pyodbc://@{path}")
            self.dataFrame = pd.read_sql_table(database,engine)
        elif type == 'postgresql':
            if port == None:
                port = '5432'
            engine = sql.create_engine(f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}")
            self.dataFrame = pd.read_sql_table(database,engine)
        elif type == 'mysql':
            if port == None:
                port = '3306'
            engine = sql.create_engine(f"mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}")
            self.dataFrame = pd.read_sql_table(database,engine)
        elif type == 'mssql':
            if port == None:
                port = '1433'
            engine = sql.create_engine(f"mssql+pyodbc://{user}:{password}@{host}:{port}/{database}")
            self.dataFrame = pd.read_sql_table(database,engine)
        elif type == 'custom':
            if port == None:
                raise TypeError("You are trying to use a custom database setup but didn't provide a port")
                
            if port == None:
                raise TypeError("You are trying to use a custom database setup but didn't provide a url")
            
            try:
                engine = sql.create_engine(url)
            except Exception:
                raise TypeError("An exception occurred when sqlalchemy tried to setup the custom databse")
                
    def get(self) -> Response:
        return self.dataFrame.to_dict()
    
    def check(self,user: str,passwordHash: str) -> Response:
        for i in range(len(self.dataFrame['user'])):
            if self.dataFrame['user'][i] == user and self.dataFrame['hash'][i] == passwordHash:
                return jsonify({'response': 'True'})
        return jsonify({'response': 'False'})