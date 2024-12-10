import sqlite3 as con

from database.session import Loja_database


class Venda:
    def table_venda():
        """
            funcao que cria a tabela venda no banco de dados
        """
        
        with open('app/sql/venda_sql/create_table_venda.sql', 'r') as file:
            sql_venda = file.read() # ler a consulta sql e armazena em uma variável para exucutar
            
        connection = con.connect(Loja_database().database_loja) # acessando o banco de dados
        cursor = connection.cursor()
        cursor.execute(sql_venda)
        connection.commit()
        cursor.close()