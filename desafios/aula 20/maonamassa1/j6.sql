select p.nome_produto, m.nome_marca, p.estoque from produtos p
inner join marcas m on p.marca_id = m.id
where m.nome_marca = 'TechWave' or m.nome_marca = 'StyleWear'