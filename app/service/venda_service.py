import sqlite3 as con
from database.session import Loja_database
from flask import jsonify

class Service_venda:
    
    def insert_venda(data: dict):
        data['status_venda'] = 1
        values_Venda = tuple(data.values())
        
        with open('app/sql/venda_sql/insert_into_venda.sql', 'r') as file:
            sql_insert_venda = file.read()
            
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_insert_venda, values_Venda)
        connection.commit()
        cursor.close()
