import sqlite3 as con

from database.session import Loja_database

class Cliente:
    def table_clientes():
        with open('app/model/Cliente/cliente.sql', 'r') as file:
    
            sql_cliente = file.read()
            
        connection = con.connect(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_cliente)
        cursor.close()
        