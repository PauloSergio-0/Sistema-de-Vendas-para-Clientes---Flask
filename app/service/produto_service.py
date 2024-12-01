import sqlite3 as con
from database.session import Loja_database


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


    def list_produto():
        
        with open('app/sql/produto_sql/list_produto.sql', 'r') as file:
            sql_list_produto = file.read()
            
            connection = con.Connection(Loja_database().database_loja)
            cursor = connection.cursor()
            cursor.execute(sql_list_produto)
            produto = cursor.fetchall()
            lista_produto = []
            
            for row in produto:
                json_produto = {
                    "id_produto": row[0],
                    "nome_produto": row[1],
                    "codigo_produto": row[2],
                    "categoria_produto": row[3],
                    "preco_produto": row[4],
                    "status_produto": row[5]
                }
                lista_produto.append(json_produto)
            
            cursor.close()
        return lista_produto