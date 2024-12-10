import sqlite3 as con

from database.session import Loja_database

class Cliente:
    def table_clientes():
        """
            funcao que cria a tabela cliente no banco de dados
        """
        with open('app/sql/cliente_sql/create_table_cliente.sql', 'r') as file:    
            sql_cliente = file.read() # ler a consulta sql e armazena em uma variável para exucutar
            
        connection = con.connect(Loja_database().database_loja) # acessando o banco de dados
        cursor = connection.cursor()
        cursor.execute(sql_cliente)
        connection.commit()
        cursor.close()
