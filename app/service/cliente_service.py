import sqlite3 as con
from database.session import Loja_database
from flask import jsonify

class Service_cliente:
    
    def insert_cliente(data: dict):
        data['status_cliente'] = 1
        values_cliente = tuple(data.values())
        
        with open('app/sql/cliente_sql/insert_into_cliente.sql', 'r') as file:
            sql_insert_cliente = file.read()
        
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_insert_cliente, values_cliente)
        connection.commit()
        cursor.close()
