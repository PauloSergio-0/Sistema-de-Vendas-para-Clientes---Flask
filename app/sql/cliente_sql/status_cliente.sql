SELECT 
	CASE 
		WHEN c.status_cliente = 0 THEN 'inativo'
		WHEN c.status_cliente = 1 THEN 'ativo'
		WHEN c.status_cliente = 9 THEN 'excluido'
        ELSE 'status não localizado'
	END AS status_cliente 
FROM cliente as  c
WHERE c.id_cliente = ?;