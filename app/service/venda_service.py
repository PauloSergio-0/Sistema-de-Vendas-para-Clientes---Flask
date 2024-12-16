import sqlite3 as con
from database.session import Loja_database
from .cliente_service import Service_cliente
from .produto_service import Service_produto
from flask import jsonify
from datetime import date
import json
class Service_venda:
    
    def _exists_vendas(id_venda: int):# verifica a existência da venad
        venda = (id_venda, )
        
        with open('app/sql/venda_sql/filter_venda.sql', 'r') as file:
            sql_filter_venda = file.read()
        try:    
            connection = con.Connection(Loja_database().database_loja)
            cursor = connection.cursor()
            cursor.execute(sql_filter_venda, venda)
            venda_filted =cursor.fetchall()
            cursor.close()
            if venda_filted:
                return True
            else: 
                return False
        except con.Error as e:
            return False
    
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
        
        try:
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

            return {"status": True, "content":lista_venda}
        
        except (Exception or con.Error) as e:
            return {"status": False, "message_error": str(e)}
    
    def filter_vendas(id_venda: int):
        venda = (id_venda, )
        
        with open('app/sql/venda_sql/filter_venda.sql', 'r') as file:
            sql_filter_venda = file.read()
            
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_filter_venda, venda)
        venda_filted = cursor.fetchall()
        cursor.close()
        
        for item in venda_filted:
            json_venda = {
                "id_venda": item[0],
                "id_cliente": item[1],
                "id_produto": item[2],
                "nome_cliente": item[3],
                "contato_cliente": item[4],
                "nome_produto": item[5],
                "categoria_produto": item[6],
                "quantidade_venda": item[7],
                "preco_produto": item[8],
                "valor_venda": item[9],
                "data_venda": item[10],
                "status_venda": item[11]
            }
            
        return json_venda
    
    def filter_date_vendas(date_venda: str):
        venda = (date_venda, )
        
        with open('app/sql/venda_sql/filter_date_venda.sql', 'r') as file:
            sql_filter_venda = file.read()
            
        connection = con.Connection(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_filter_venda, venda)
        venda_filted =cursor.fetchall()
        cursor.close()
        venda_date_filted = []
        for item in venda_filted:
            json_venda_date = {
                "id_venda": item[0],
                "id_cliente": item[1],
                "id_produto": item[2],
                "nome_cliente": item[3],
                "contato_cliente": item[4],
                "nome_produto": item[5],
                "categoria_produto": item[6],
                "quantidade_venda": item[7],
                "preco_produto": item[8],
                "valor_venda": item[9],
                "data_venda": item[10],
                "status_venda": item[11]
            }
            venda_date_filted.append(json_venda_date)
            
        return venda_date_filted
    
    def delete_venda(id_venda: int):
        
        venda = (id_venda, )
        
        with open('app/sql/venda_sql/delete_venda.sql', 'r') as file:
            sql_delete_venda = file.read()
        
        try:
            if Service_venda._exists_vendas(id_venda):
                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_delete_venda, venda)
                connection.commit()
                cursor.close()
                return f'Venda com id {id_venda} excluída'
            else:
                return f'Venda com id {id_venda} não existe'
            
        except con.Error:
            return 'error in query' 

    def cancel_venda(id_venda: int):
        
        venda = (id_venda, )
        
        with open('app/sql/venda_sql/cancel_venda.sql', 'r') as file:
            sql_cancel_venda = file.read()
        
        try:
            if Service_venda._exists_vendas(id_venda):
                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_cancel_venda, venda)
                connection.commit()
                cursor.close()
                return f'Venda com id {id_venda} cancelada'
            else:
                return f'Venda com id {id_venda} não existe'
            
        except con.Error:
            return 'error in query'    
        
    
    def sale_venda(data: dict):# realiza a venda
        
        produto_validated = Service_produto._produto_status(data['id_produto'])# retorna o status do produto se existir
        cliente_validated = Service_cliente._cliente_status(data['id_cliente'])# retorna o status do cliente se existir
        
        exists_produto_venda: bool = (produto_validated['result']  and cliente_validated['result']) # variavel apenas com valor que retorna a existencia ou não do produto e venda
        
        if exists_produto_venda :
            # se ambos existirem avança para a proxima condicional que verificar se os ststus estão aptos para a venda
            if (produto_validated["status_produto"] == 'ativo') and (cliente_validated['status_cliente'] == 'ativo'):
                
                data['status_venda'] = 1
                values_Venda = tuple(data.values())
                
                with open('app/sql/venda_sql/insert_into_venda.sql', 'r') as file:
                    sql_insert_venda = file.read()
                    
                connection = con.Connection(Loja_database().database_loja)
                cursor = connection.cursor()
                cursor.execute(sql_insert_venda, values_Venda)
                connection.commit()
                cursor.close()
            
                return {"status": True, "message": "Venda concluída com sucesso"}

            else:
                for key, values in {"Produto":  produto_validated["status_produto"], "Cliente": cliente_validated['status_cliente']}.items():
                    if not values  == 'ativo':
                        return {"status": False, "message": f"o {key} não é válido para realizar venda.",
                                "status_elemento": f"{values}"}
        else:
            if not exists_produto_venda:
                for key, values in {"Produto": produto_validated['result'], "Cliente": cliente_validated['result']}.items():
                    if not values:
                        return {"status": False, "message": f"o {key} não existe para realizar venda"}
            
