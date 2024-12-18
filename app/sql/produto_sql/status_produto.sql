SELECT  
	CASE 
		WHEN p.status_produto = 0 THEN 'inativo'
		WHEN p.status_produto = 1 THEN 'ativo'
		WHEN p.status_produto = 9 THEN 'excluido'
		ELSE 'status não localizado'
	END as status_produto
FROM produto p
WHERE p.id_produto = ?;


