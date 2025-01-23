# Sistema de vendas para Clientes

```
└── 📁app
    └── 📁database --inicia o banco de dados
        └── __init__.py
        └── session.py
    └── 📁decorators --funções decoradas
        └── jwt_required.py
    └── 📁logs --armazenamento de logs
    └── 📁Loja_Database --database-fisico
        └── loja.db
    └── 📁model --modelagem do banco de dados
        └── __init__.py
            └── __init__.cpython-313.pyc
        └── 📁Cliente
            └── __init__.py
                └── __init__.cpython-313.pyc
                └── clientes_model.cpython-313.pyc
            └── clientes_model.py
        └── 📁Produto
                └── produtos_model.cpython-313.pyc
            └── produtos_model.py
        └── 📁Venda
                └── vendas_model.cpython-313.pyc
            └── vendas_model.py
    └── 📁routes --rotas da AOI
        └── __init__.py
        └── authorization_routes.py
        └── cliente_routes.py
        └── produto_routes.py
        └── test_routes.py
        └── venda_routes.py
    └── 📁service --Funções para as rotas
        └── __init__.py
        └── cliente_service.py
        └── produto_service.py
        └── venda_service.py
    └── 📁settings --Configutações da API (logs, app , database)
        └── __init__.py
        └── config.py
        └── flask_app.py
        └── jwt_config.py
        └── logs_app.py
    └── 📁sql --consultas SQLs
        └── 📁cliente_sql
            └── create_table_cliente.sql
            └── delete_cliente.sql
            └── desactivate_cliente.sql
            └── filter_cliente.sql
            └── insert_into_cliente.sql
            └── list_cliente.sql
            └── status_cliente.sql
        └── 📁produto_sql
            └── create_table_produto.sql
            └── delete_produto.sql
            └── desactivate_produto.sql
            └── filter_produto.sql
            └── insert_into_produto.sql
            └── list_produto.sql
            └── status_produto.sql
        └── 📁venda_sql
            └── cancel_venda.sql
            └── create_table_venda.sql
            └── delete_venda.sql
            └── filter_date_venda.sql
            └── filter_venda.sql
            └── insert_into_venda.sql
            └── list_venda.sql
            └── status_venda.sql
    └── 📁utils --Validadores
        └── __init__.py
        └── auth_service.py
        └── json_validator.py
    └── run.py --execução
```