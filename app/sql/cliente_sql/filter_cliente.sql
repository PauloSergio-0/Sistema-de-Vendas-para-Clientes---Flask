SELECT 
	c.id_cliente,
	c.nome,
	c.endereco,
	c.contato,
	CASE 
		WHEN c.status_cliente = 0 THEN 'desativado'
		WHEN c.status_cliente = 1 THEN 'ativo'
		WHEN c.status_cliente = 9 THEN 'excluido'
	END AS status_cliente 
FROM cliente c
WHERE c.id_cliente = ?;