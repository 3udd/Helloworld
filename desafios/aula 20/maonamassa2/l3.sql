select m.nome_marca, p.nome_produto from produtos p
left join marcas m on p.marca_id = m.id