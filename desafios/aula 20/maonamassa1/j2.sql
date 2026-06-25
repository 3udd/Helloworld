select p.nome_produto, p.preco, m.pais_origem from produtos p
inner join marcas m on p.marca_id = m.id