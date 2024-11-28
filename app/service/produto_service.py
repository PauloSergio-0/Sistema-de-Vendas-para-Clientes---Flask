import sqlite3 as con
from database.session import Loja_database
from flask import jsonify

class Service_produto:
    
    def insert_produto(data: dict):
        data['status_produto'] = 1
        values_Produto = tuple(data.values())
        
        with open('app/sql/produto_sql/insert_into_produto.sql', 'r') as file:
            sql_insert_produto = file.read()
            
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_insert_produto, values_Produto)
        connection.commit()
        cursor.close()
