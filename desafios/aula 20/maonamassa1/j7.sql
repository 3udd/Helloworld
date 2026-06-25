select p.nome_produto, m.nome_marca from produtos p
inner join marcas m on p.marca_id = m.id
order by p.preco desc limit 1