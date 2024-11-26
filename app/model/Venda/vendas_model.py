import sqlite3 as con

from database.session import Loja_database


class Venda:
    def table_venda():
        with open('app/sql/venda_sql/create_table_venda.sql', 'r') as file:
            sql_venda = file.read()
            
        connection = con.connect(Loja_database().database_loja)
        cursor = connection.cursor()
        cursor.execute(sql_venda)
        connection.commit()
        cursor.close()