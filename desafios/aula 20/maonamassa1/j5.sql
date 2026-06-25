select p.nome_produto, p.preco from produtos p
inner join marcas m on p.marca_id = m.id
where m.pais_origem = 'Brasil'