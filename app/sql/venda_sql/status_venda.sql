SELECT
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
WHERE v.id_venda = ?; 