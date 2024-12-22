import sqlite3 as con
from database.session import Loja_database
from flask import jsonify, json

class Service_cliente:
    
    def _exists_cliente(id_cliente: int):# verifica se existe o cliente 
        try:
            value = (id_cliente,)
            
            with open('app/sql/cliente_sql/status_cliente.sql', 'r') as file:
                sql_filter_cliente = file.read()

            connection = con.Connection(Loja_database().database_loja)
            cursor = connection.cursor()
            cursor.execute(sql_filter_cliente, value)
            cliente = cursor.fetchall()[0]
            cursor.close()
            if cliente:
                return {'status': True, 'content': cliente[0]}
            else:
                return {'status': False}
        except:
            return {'status': False}
    
    def _cliente_status(id_cliente: int): # verifica o status do cliente
        
        if Service_cliente._exists_cliente(id_cliente):
            cliente = Service_cliente.filter_cliente(id_cliente)
            return {'result': True, 'status_cliente': cliente['content']}
        else:
            return {"result": False}
    
    def insert_cliente(data: dict): 
        
        """
            Esse metodo é  responsavel pela a inserção no banco de dados
        
        """
        try:
            data["status_cliente"] = 1
            values_cliente = tuple(data.values())
            
            with open('app/sql/cliente_sql/insert_into_cliente.sql', 'r') as file:
                sql_insert_cliente = file.read()
            
            connection = con.Connection(Loja_database().database_loja)
            cursor = connection.cursor()
            cursor.execute(sql_insert_cliente, values_cliente)
            connection.commit()
            cursor.close()
            
            return {"status": True, 'message': "Cliente cadastrado"}
        
        except (Exception or con.Error) as e:
            return {"status": False, 'message_error': str(e)}

    
    def list_cliente(): # lista todos os clientes idependente do status
        try:
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
            
            return {'status': True, 'content': lista_clientes}

        except (Exception or con.Error) as e:
            return {'status': False, 'message_error': str(e)}
            

    def filter_cliente(id_cliente: int): # filtra pelo id 
        
        try:
            id_cliente = int(id_cliente)
            if not isinstance(id_cliente, int):
                return{"status": False, "message_error" : f'Tipo não aceito: {type(id_cliente)}'}
            
            value = (id_cliente,)
            
            with open('app/sql/cliente_sql/filter_cliente.sql', 'r') as file:
                sql_filter_cliente = file.read()
            
            connection = con.Connection(Loja_database().database_loja)
            cursor = connection.cursor()
            cursor.execute(sql_filter_cliente, value)
            cliente = cursor.fetchall()
            cursor.close()
                
            if not cliente:
                return {"status": False, "message_error" : f'Não existe cliente com esse id: {id_cliente}'}
            
            for item in cliente:
                json_lista_cliente = {
                    "id_cliente": item[0],
                    "nome_cliente": item[1],
                    "endereco_cliente": item[2],
                    "contato_cliente": item[3],
                    "status_cliente": item[4]
                }
                
            return {"status": True, "content" :json_lista_cliente}

        except (Exception or con.Error) as e:
            return {"status": False, "message_error" : str(e)}


    def delete_cliente(id_cliente: int):# deleta logicamente

        try:
            cliente_valitaded = Service_cliente._exists_cliente(id_cliente)
            

            valid_status_del = ('ativo', 'inativo')

            if cliente_valitaded['status'] and cliente_valitaded['content'] in valid_status_del:
                cliente = (id_cliente, )

                with open("app/sql/cliente_sql/delete_cliente.sql", 'r') as file:
                    sql_delete_cliente = file.read()

                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_delete_cliente, cliente)
                connection.commit()
                cursor.close()

                return {"status": True, "message": f"O cliente {id_cliente} foi excluído"}
            else:

                if not cliente_valitaded['status']:
                    return {"status": False, "message_error": f'Não existe cliente com esse id: {id_cliente}'}

                elif not cliente_valitaded['content'] in valid_status_del:
                    return {"status": False, "message_error": f'Status não autorizado para exclusão'}

        except (Exception or con.Error) as e:
                return {"status": False, "message_error": {str(e)}}

    def desactivate_cliente( id_cliente: str):# desativa logicamente
        try:
            cliente_valitaded = Service_cliente._exists_cliente(id_cliente)

            if cliente_valitaded['status'] and cliente_valitaded['content'] == 'ativo':
                cliente = (id_cliente, )

                with open("app/sql/cliente_sql/desactivate_cliente.sql", 'r') as file:
                    sql_desactivate_cliente = file.read()

                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_desactivate_cliente, cliente)
                connection.commit()
                cursor.close()
                
                return {"status": True, "message": f"O cliente {id_cliente} foi desativado"}

            else:
                if not cliente_valitaded['status']:
                    return {"status": False, "message_error": f'Não existe cliente com esse id: {id_cliente}'}
                
                elif not cliente_valitaded['content'] == 'ativo':
                    return {"status": False, "message_error": f'Status não autorizado para desativação.'}

        except (Exception or con.Error) as e:
                return {"status": False, "message_error": str(e)}
