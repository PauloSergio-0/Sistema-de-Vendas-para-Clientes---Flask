import sqlite3 as con
from database.session import Loja_database
from flask import jsonify, json

class Service_cliente:
    
    def exists_cliente(id_cliente: int):
        value = (id_cliente,)
        
        with open('app/sql/cliente_sql/filter_cliente.sql', 'r') as file:
            sql_filter_cliente = file.read()

        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_filter_cliente, value)
        cliente = cursor.fetchall()
        cursor.close()
        if cliente:
            return True
        else:
            return False
    
    
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

    def filter_cliente(id_cliente: int):
        value = (id_cliente,)
        
        with open('app/sql/cliente_sql/filter_cliente.sql', 'r') as file:
            sql_filter_cliente = file.read()

        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_filter_cliente, value)
        cliente = cursor.fetchall()
        cursor.close()
        if not cliente:
            return "Cliente não existe"
        else:
            for item in cliente:
                json_lista_cliente = {
                    "id_cliente": item[0],
                    "nome_cliente": item[1],
                    "endereco_cliente": item[2],
                    "contato_cliente": item[3],
                    "status_cliente": item[4]
                }
            return json_lista_cliente
        
    
    
    def delete_cliente( id_cliente: str):
        
        if Service_cliente.exists_cliente(id_cliente):
            cliente = (id_cliente, )
            
            with open("app/sql/cliente_sql/delete_cliente.sql", 'r') as file:
                sql_delete_cliente = file.read()
                
            try:
                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_delete_cliente, cliente)
                connection.commit()
                cursor.close()
                return f"O cliente {id_cliente} foi excluído"
            except con.Error as e:
                return "Error in database query"
            
        else:
            return f'Não existe cliente com esse id: {id_cliente}'
        