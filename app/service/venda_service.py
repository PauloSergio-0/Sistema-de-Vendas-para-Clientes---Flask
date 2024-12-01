import sqlite3 as con
from database.session import Loja_database
from flask import jsonify
import json
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

    def list_venda():
        
        with open('app/sql/venda_sql/list_venda.sql', 'r') as file:
            sql_list_venda = file.read()
        
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_list_venda)
        venda = cursor.fetchall()
        lista_venda = []
        for row in venda:
            json_venda = {
                "id_venda": row[0],
                "id_cliente": row[1],
                "id_produto": row[2],
                "nome_cliente": row[3],
                "contato_cliente": row[4],
                "nome_produto": row[5],
                "categoria_produto": row[6],
                "quantidade_venda": row[7],
                "preco_produto": row[8],
                "valor_venda": row[9],
                "data_venda": row[10],
                "status_venda": row[11]
            }
            lista_venda.append(json_venda)
        cursor.close()  

        return lista_venda