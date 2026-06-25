select c.nome_cliente, p.data_pedido, p.status from pedidos p
inner join clientes c on p.cliente_id = c.id