import sqlite3 as con
from database.session import Loja_database
from flask import jsonify, json

class Service_cliente:
    
    def insert_cliente(data: dict):
        data["status_cliente"] = 1
        values_cliente = tuple(data.values())
        
        with open('app/sql/cliente_sql/insert_into_cliente.sql', 'r') as file:
            sql_insert_cliente = file.read()
        
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_insert_cliente, values_cliente)
        connection.commit()
        cursor.close()

    
    def list_cliente():
        
        with open('app/sql/cliente_sql/list_cliente.sql', 'r') as file:
            sql_list_cliente = file.read()
            
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_list_cliente)
        clientes = cursor.fetchall()
        lista_clientes = []
        for row in clientes:
            json_lista_cliente = {
                "id_cliente": row[0],
                "nome_cliente": row[1],
                "endereco_cliente": row[2],
                "contato_cliente": row[3],
                "status_cliente": row[4]
            }
            lista_clientes.append(json_lista_cliente)
        cursor.close()
        
        return lista_clientes
