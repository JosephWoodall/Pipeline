import logging
import sys
from sqlalchemy import create_engine
from config.config import config_keys


class Connection():
    
    """Establishes the connection for the selected database
    """
    
    def __init__(self, database):
        self.handler = logging.FileHandler('logs/projectLogs.log')
        self.handler.setLevel(logging.DEBUG)
        self.database = database
        
        if self.database: 
            self.engine = config_keys.get('dataWarehouseEngine')
            self.user = config_keys.get('dataWarehouseSecretUser')
            self.password = config_keys.get('dataWarehouseSecretPassword')
            self.url = config_keys.get('dataWarehouseUrl')
            self.port = config_keys.get('dataWarehousePort')
            self.db = config_keys.get('dataWarehouseDb')
        else:
            print("Please provide correct DB access credentials and try again.")
            sys.exit()
        
        self.sql_connection_string = f"{self.engine}://{self.user}:{self.password}@{self.url}:{self.port}/{self.db}?trusted_connection=yes"
        logging.getLogger("Connection class Initialization").addHandler(self.handler)
    
    def connection(self):
        engine = create_engine(f'{self.sql_connection_string}')
        self.conn = engine.connect()
        self.cur = self.conn.cursor()
        logging.getLogger('Connection.connection() call').addHandler(self.handler)
        return self.cur

    
        