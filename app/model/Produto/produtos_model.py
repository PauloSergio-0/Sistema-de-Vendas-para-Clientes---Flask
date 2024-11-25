import sqlite3 as con

from database.session import Loja_database

class Produto:
    def table_produto():
        with open('app/model/Produto/produto.sql', 'r') as file:
            sql_produto = file.read()
        
        connection = con.connect(Loja_database().database_loja)
        curso = connection.cursor()
        curso.execute(sql_produto)
        curso.close()