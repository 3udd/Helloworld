select c.nome_cliente, m.nome_marca from marcas m
inner join produtos pr on m.id = pr.marca_id
inner join itens_compra ic on pr.id = ic.produto_id
inner join pedidos pe on ic.pedido_id = pe.id
inner join clientes c on pe.cliente_id = c.id