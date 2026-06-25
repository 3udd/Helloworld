select p.nome_produto, m.nome_marca from produtos p
left join marcas m on p.marca_id = m.id