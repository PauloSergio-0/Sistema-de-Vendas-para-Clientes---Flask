CREATE TABLE IF NOT EXISTS produto (
    id_produto INTEGER PRIMARY KEY AUTOINCREMENT,
    nome VARCHAR NOT NULL,
    codigo VARCHAR NOT NULL,
    categoria VARCHAR NOT NULL,
    preco REAL NOT NULL,
    status_produto INTEGER NOT NULL
);