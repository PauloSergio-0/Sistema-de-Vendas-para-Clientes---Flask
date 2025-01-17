SELECT  
	p.id_produto,
	p.nome,
	p.codigo,
	p.categoria,
	p.preco,
	CASE 
		WHEN p.status_produto = 0 THEN 'desativado'
		WHEN p.status_produto = 1 THEN 'ativo'
		WHEN p.status_produto = 9 THEN 'excluido'
		ELSE 'status não localizado'
	END as status_produto
FROM produto p
WHERE p.id_produto = ?; 