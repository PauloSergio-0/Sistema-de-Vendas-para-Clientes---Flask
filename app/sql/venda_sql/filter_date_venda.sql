SELECT
	v.id_venda,
	v.id_cliente,
	c.nome AS nome_cliente,
	c.contato AS contato_cliente,
	v.id_produto,
	p.nome AS nome_produto,
	p.categoria AS categoria_produto,
	p.preco AS preco_produto,
	v.qtd_venda,
	ROUND(p.preco * v.qtd_venda, 2) AS valor_venda,
	v.data_venda,
	CASE
		WHEN v.status_vendas = 0 THEN 'cancelada'
		WHEN v.status_vendas = 1 THEN 'processando'
		WHEN v.status_vendas = 2 THEN 'cancelada pelo cliente'
		WHEN v.status_vendas = 3 THEN 'prazo de pagamento expirado'
		WHEN v.status_vendas = 4 THEN 'cancelado pelo intermediador'
		WHEN v.status_vendas = 9 THEN 'excluida'
		ELSE 'status_desconhecido'
	END AS status_venda
FROM  venda v
INNER JOIN produto p ON p.id_produto = v.id_produto
INNER JOIN cliente c ON c.id_cliente = v.id_cliente
WHERE DATE(v.data_venda) = ?; 