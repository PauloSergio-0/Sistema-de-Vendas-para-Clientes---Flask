from flask import Flask

from database.session import Loja_database

from model.Cliente.clientes_model import Cliente
from model.Produto.produtos_model import Produto
from model.Venda.vendas_model import Venda

from routes import routes_flask


def create_app():
    """
    Função reposnsavel por inicializar o app Flask junto com o banco de dados

    Returns:
        _type_: _description_
    """
    app = Flask(__name__)
    
    Loja_database()._database()

    if Loja_database().exist_db():


        Cliente.table_clientes()
        Produto.table_produto()
        Venda.table_venda()
        
    routes_flask(app)
    return app
