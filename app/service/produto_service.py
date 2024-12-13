import sqlite3 as con
from database.session import Loja_database


class Service_produto:
    
    
    def _exists_produto(id_produto: int):# verifica a existencia do produto
        produto = (id_produto, )
        
        with open('app/sql/produto_sql/filter_produto.sql', 'r') as file:
            sql_filter_produto = file.read()
        try:
            connection = con.Connection(Loja_database().database_loja)
            cursor = connection.cursor()
            cursor.execute(sql_filter_produto, produto)
            produto_filted = cursor.fetchall()
            cursor.close()
            if produto_filted:
                return True
            else:
                return False
        except con.Error as e:
            return False
            
            
    def _produto_status(id_produto: int):# retorna o status se o produto existir
        
        if Service_produto._exists_produto(id_produto):
            produto = Service_produto.filter_produto(id_produto)
            return {'result': True, 'status_produto':produto['status_produto']}
        else:
            return {'result': False}
        
        
    def insert_produto(data: dict): # insere produto no banco de dados
        
        data['status_produto'] = 1 # adciona o status automáticamente como 1: ativado
        values_Produto = tuple(data.values())
        
        with open('app/sql/produto_sql/insert_into_produto.sql', 'r') as file:
            sql_insert_produto = file.read()
            
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_insert_produto, values_Produto)
        connection.commit()
        cursor.close()


    def list_produto(): # retornar todos os produtos
        
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


    def filter_produto(id_produto: int):
        produto = (id_produto, )
        
        with open('app/sql/produto_sql/filter_produto.sql', 'r') as file:
            sql_filter_produto = file.read()
            
        
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_filter_produto, produto)
        produto_filted = cursor.fetchall()
        cursor.close()
        if produto_filted:
            for item in produto_filted:
                json_produto = {
                        "id_produto": item[0],
                        "nome_produto": item[1],
                        "codigo_produto": item[2],
                        "categoria_produto": item[3],
                        "preco_produto": item[4],
                        "status_produto": item[5]
                    }
            return json_produto
        else:
            return f"produto com id {id_produto} não existe"
        
    
    def delete_produto(id_produto: int):
        
        produto = (id_produto, )
        
        with open('app/sql/produto_sql/delete_produto.sql', 'r') as file:
            sql_delete_produto = file.read()
        try:    
            if Service_produto._exists_produto(id_produto):
                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_delete_produto, produto)
                connection.commit()
                cursor.close()
                return f"produto com id {id_produto} excluído"
            else:
                return f"produto com id {id_produto} não existe"
        except con.Error as e:
            return 'erro in query'
        
    def desactivate_produto(id_produto: int):
        
        produto = (id_produto, )
        
        with open('app/sql/produto_sql/desactivate_produto.sql', 'r') as file:
            sql_desactivate_produto = file.read()
        try:    
            if Service_produto._exists_produto(id_produto):
                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_desactivate_produto, produto)
                connection.commit()
                cursor.close()
                return f"produto com id {id_produto} desativado"
            else:
                return f"produto com id {id_produto} não existe"
        except con.Error as e:
            return 'erro in query'