from database.session import Loja_database

from model.Cliente.clientes_model import Cliente
from model.Produto.produtos_model import Produto
from model.Venda.vendas_model import Venda

Loja_database()._database()
print(Loja_database().exist_db())
print(Loja_database().database_loja)


print(Cliente.table_clientes())
print(Produto.table_produto())
print(Venda.table_venda())