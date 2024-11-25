import sqlite3 as con
import os
from settings.config import Config

class Loja_database:
    def __init__(self):
        self.url_db = Config.URL_DB
        self.database_loja = str(self.url_db + '/' + Config.DATABASE)

    def _database(self):
        
        if os.path.exists(self.url_db):
            con.connect(self.database_loja)
        else:
            os.makedirs(self.url_db,exist_ok=True)
            con.connect(self.database_loja)

    def exist_db(self):
        
        if os.path.exists(self.database_loja):
            return True
        else: 
            return False