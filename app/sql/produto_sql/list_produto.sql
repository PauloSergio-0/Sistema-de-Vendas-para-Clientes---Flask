SELECT 
	p.id_produto,
	p.nome,
	p.codigo,
	p.categoria,
	p.preco,
	CASE 
		WHEN p.status_produto = 1 THEN 'ativo'
		WHEN p.status_produto = 0 THEN 'inativo'
		WHEN p.status_produto = 9 THEN 'excluido'
		ELSE 'status desconhecido'
	END AS status_produto 
FROM produto p;