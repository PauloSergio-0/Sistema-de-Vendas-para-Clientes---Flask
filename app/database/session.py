import sqlite3 as con
import os
from settings.config import Config

class Loja_database:
    
    """Iniciando o database:
            acessa o local onde o bando de dados deve ficar e qual deve ser o nome do banco de dados.

            Caso o banco não exista ele será criado.
        
    """
    def __init__(self):
        self.url_db = Config.URL_DB # "app/Loja_Database/"
        self.database_loja = str(self.url_db + Config.DATABASE) # Config.DATABASE: "loja.db"

    def _database(self):
        
        """verifica se o local do banco existe para iniciá-lo
            se não o local será criado para ter a criação do arquivo '.db'"""
        
        if os.path.exists(self.url_db):
            con.connect(self.database_loja)
        else:
            os.makedirs(self.url_db,exist_ok=True)
            con.connect(self.database_loja)

    def exist_db(self):
        # Função que verifica a existência do banco
        if os.path.exists(self.database_loja):
            return True
        else: 
            return False