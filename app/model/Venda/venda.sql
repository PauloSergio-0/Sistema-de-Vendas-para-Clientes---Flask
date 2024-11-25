CREATE TABLE IF NOT EXISTS venda (
    id_venda INTEGER PRIMARY KEY AUTOINCREMENT,
    id_cliente INTEGER NOT NULL,
    id_produto INTEGER NOT NULL,
    qtd_venda INTEGER NOT NULL,
    data_venda DATE NOT NULL,
    status_vendas INTEGER NOT NULL,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente),
    FOREIGN KEY (id_produto) REFERENCES produto(id_produto)
);