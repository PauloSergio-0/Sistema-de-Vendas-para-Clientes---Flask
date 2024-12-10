import sqlite3 as con

from database.session import Loja_database

class Produto:
    def table_produto():
        
        """
            funcao que cria a tabela produto no banco de dados
        """
        
        with open('app/sql/produto_sql/create_table_produto.sql', 'r') as file:
            sql_produto = file.read() # ler a consulta sql e armazena em uma variável para exucutar
        
        connection = con.connect(Loja_database().database_loja) # acessando o banco de dados
        curso = connection.cursor()
        curso.execute(sql_produto)
        connection.commit()
        curso.close()
