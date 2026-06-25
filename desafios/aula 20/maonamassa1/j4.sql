select m.nome_marca, p.nome_produto, p.preco from produtos p
inner join marcas m on p.marca_id = m.id
order by m.nome_marca asc, p.preco desc