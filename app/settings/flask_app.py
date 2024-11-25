from flask import Flask

from database.session import Loja_database
from routes.test_routes import register_routes
from model.Cliente.clientes_model import Cliente
from model.Produto.produtos_model import Produto
from model.Venda.vendas_model import Venda



def create_app():
    app = Flask(__name__)
    
    Loja_database()._database()

    if Loja_database().exist_db():


        Cliente.table_clientes()
        Produto.table_produto()
        Venda.table_venda()
        
    register_routes(app)
    
    return app
