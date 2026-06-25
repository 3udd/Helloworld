select pr.nome_produto, (preco_unitario * quantidade) as valor_total from itens_compra ic
inner join produtos pr on ic.produto_id = pr.id