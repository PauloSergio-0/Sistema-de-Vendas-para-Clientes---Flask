import sqlite3 as con
import os
from settings.config import Config

class Loja_database:
    def __init__(self):
        self.url_db = Config.URL_DB
        self.database_loja = self.url_db+Config.DATABASE
        
    def _database(self):
        if os.path.exists(self.database_loja):
            connection_db = con.connect(self.database_loja)
        else:
            os.makedirs(self.database_loja)
        
        
    
        
if __name__ == '__main__':
    print(Loja_database().url_db)