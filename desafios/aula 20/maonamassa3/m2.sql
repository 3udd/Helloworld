select c.nome_cliente, pr.nome_produto, ic.quantidade from itens_compra ic
inner join pedidos pe on ic.pedido_id = pe.id 
inner join clientes c on pe.cliente_id = c.id
inner join produtos pr on ic.produto_id = pr.id