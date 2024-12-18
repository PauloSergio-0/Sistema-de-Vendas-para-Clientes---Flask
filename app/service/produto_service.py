import sqlite3 as con
from database.session import Loja_database


class Service_produto:
    
    def _exists_produto(id_produto: int):# verifica a existencia do produto
        produto = (id_produto, )
        
        with open('app/sql/produto_sql/status_produto.sql', 'r') as file:
            sql_filter_produto = file.read()
        try:
            connection = con.Connection(Loja_database().database_loja)
            cursor = connection.cursor()
            cursor.execute(sql_filter_produto, produto)
            produto_filted = cursor.fetchall()
            cursor.close()
            
            if produto_filted:
                return {'status': True, 'content': produto_filted}
            
            else:
                return {'status': False}
            
        except con.Error as e:
            return {'status': False}
            
            
    def insert_produto(data: dict): # insere produto no banco de dados
        try:
            data['status_produto'] = 1 # adciona o status automáticamente como 1: ativo
            values_Produto = tuple(data.values())
            
            with open('app/sql/produto_sql/insert_into_produto.sql', 'r') as file:
                sql_insert_produto = file.read()
                
            connection = con.Connection(Loja_database().database_loja)
            cursor = connection.cursor()
            cursor.execute(sql_insert_produto, values_Produto)
            connection.commit()
            cursor.close()
            
            return {'status': True, 'message' : "Produto cadastrado"}
            
        except (Exception or con.Error) as e:
            return {'status': False, 'message_error': str(e)}


    def list_produto(): # retornar todos os produtos
        try:
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
                
            return {'status': True, 'content': lista_produto}
        
        except (Exception or con.Error) as e: 
            return {'status': False, 'message_error': str(e)}     

    def filter_produto(id_produto: int):
        
        try:
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

                return {'status': True, 'content': json_produto}

            else:
                return {'status': False, 'message_error': f"produto com id {id_produto} não existe"}
            
        except (Exception or con.Error) as e:
            return {'status': False, 'message_error': str(e)}
    
    def delete_produto(id_produto: int):
        try:

            status_produto = Service_produto._exists_produto(id_produto)
            produto_del = ('ativo', 'inativo')
            produto = (id_produto, )
            
            with open('app/sql/produto_sql/delete_produto.sql', 'r') as file:
                sql_delete_produto = file.read()

                if status_produto['status'] and status_produto['content'] in produto_del:
                    
                    connection = con.Connection(Loja_database().database_loja)
                    cursor = connection.cursor()
                    cursor.execute(sql_delete_produto, produto)
                    connection.commit()
                    cursor.close()
                    return {'status': True, 'message': f"produto com id {id_produto} excluído"}
                
                else:
                    if not status_produto['status']:
                        return {'status': False, 'message_error': f"produto com id {id_produto} não existe"}
                    
                    elif not status_produto['content'] in produto_del:
                        return {'status': False, 'message_error': f"produto com id {id_produto} não é valido para excluir"}

        except (Exception or con.Error) as e:
            return {'status': False, 'message_error': str(e)}
        
    def desactivate_produto(id_produto: int):
        try:
            status_produto = Service_produto._exists_produto(id_produto)
            
            if status_produto['status'] and status_produto['content'] == 'ativo':
                produto = (id_produto, )
                
                with open('app/sql/produto_sql/desactivate_produto.sql', 'r') as file:
                    sql_desactivate_produto = file.read()

                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_desactivate_produto, produto)
                connection.commit()
                cursor.close()
                
                return {'status': True, 'message': f"produto com id {id_produto} desativado"}
            
            else:
                if not status_produto['result']:
                    return {'status': False, 'message_error': f"produto com id {id_produto} não existe"}
                
                elif not status_produto['status_produto'] == 'ativo':
                        return {'status': False, 'message_error': f"produto com id {id_produto} não é valido para inativar"}
                    
        except (Exception or con.Error) as e:
            return {'status': False, 'message_error': str(e)}