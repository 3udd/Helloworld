import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"



@app.get('/l1')
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    select p.nome_produto, m.nome_marca from produtos p
                    left join marcas m on p.marca_id = m.id
                  """
            resultado = con.execute(text(sql))
            linhas_banco = resultado.fetchall()
            consultas = []

            for row in linhas_banco:
                linha = row._mapping
                consulta = {
                    "nome do produto": linha['nome_produto'],
                    "data da marca": linha['nome_marca']
                }
                consultas.append(consulta)
            return consultas
            
    except Exception as e:
        return f"erro no banco {e}"


@app.get('/m2')
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    select c.nome_cliente, pr.nome_produto, ie.quantidade from itens_compra ie
                    inner join pedidos pe on ie.id_pedido = pe.id_pedido 
                    inner join clientes c on pe.id_cliente = c.id_cliente
                    inner join produtos pr on ie.id_produto = pr.id_produto
                  """
            resultado = con.execute(text(sql))
            linhas_banco = resultado.fetchall()
            consulta = []

            for row in linhas_banco:
                linha = row._mapping
                consulta = {
                    "nome do cliente": linha['nome_cliente'],
                    "nome do produto": linha['nome_produto'],
                    "quantidade": linha['quantidade']
                }
                consulta.append(consulta)
            return consulta
            
    except Exception as e:
        return f"erro no banco {e}"


@app.get('/m3')
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    select pr.nome_produto, (preco_unitario * quantidade) as valor_total from itens_compra ic
                    inner join produtos pr on ic.id_produto = pr.id_produto
                  """
            resultado = con.execute(text(sql))
            linhas_banco = resultado.fetchall()
            consultas = []

            for row in linhas_banco:
                linha = row._mapping
                consulta = {
                    "nome do produto": linha['nome_produto'],
                    "valor total da compra": linha['valor_total']
                }
                consultas.append(consulta)
            return consultas
            
    except Exception as e:
        return f"erro no banco {e}"



@app.get('/m4')
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    select c.nome_cliente, m.nome_marca from marcas m
                    inner join produtos pr on m.id_marca = pr.id_marca
                    inner join itens_compra ie on pr.id_produto = ie.id_produto
                    inner join pedidos pe on ie.id_pedido = pe.id_pedido
                    inner join clientes c on pe.id_cliente = c.id_cliente
                  """
            resultado = con.execute(text(sql))
            linhas_banco = resultado.fetchall()
            consultas = []

            for row in linhas_banco:
                linha = row._mapping
                consulta = {
                    "nome do cliente": linha['nome_cliente'],
                    "nome da marca": linha['nome_marca']
                }
                consultas.append(consulta)
            return consultas
            
    except Exception as e:
        return f"erro no banco {e}"



@app.get('/m5')
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    select c.id_cliente, c.nome_cliente, c.email from clientes c
                    left join pedidos p on c.id_cliente = p.id_cliente
                    where p.id_pedido is null
                  """
            resultado = con.execute(text(sql))
            linhas_banco = resultado.fetchall()
            consultas = []

            for row in linhas_banco:
                linha = row._mapping
                consulta = {
                    "id do cliente": linha ['id_cliente'],
                    "nome do cliente": linha['nome_cliente'],
                    "email do cliente": linha['email']
                }
                consultas.append(consulta)
            return consultas
            
    except Exception as e:
        return f"erro no banco {e}"
    


@app.get('/m6')
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    select p.nome_produto, sum(ic.quantidade) as quantidade_total from produtos p 
                    left join itens_compra ic on p.id_produto = ic.id_produto
                    group by p.nome_produto
                  """
            resultado = con.execute(text(sql))
            linhas_banco = resultado.fetchall()
            consultas = []

            for row in linhas_banco:
                linha = row._mapping
                consulta = {
                    "nome do produto": linha ['nome_produto'],
                    "quantidade total vendida": linha['quantidade_total']
                }
                consultas.append(consulta)
            return consultas
            
    except Exception as e:
        return f"erro no banco {e}"
    

@app.get('/m7')
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    select m.nome_marca, max(p.preco) as maior from produtos p
                    right join marcas m on p.id_marca = m.id_marca
                    group by m.nome_marca
                    order by m.nome_marca
                  """
            resultado = con.execute(text(sql))
            linhas_banco = resultado.fetchall()
            consultas = []

            for row in linhas_banco:
                linha = row._mapping
                consulta = {
                    "nome da marca": linha ['nome_marca'],
                    "produto mais vendido:": linha['maior']
                }
                consultas.append(consulta)
            return consultas
            
    except Exception as e:
        return f"erro no banco {e}"


if __name__ == '__main__':
    uvicorn.run(
        'maonamassa2:app',
        port=80,
        reload=True
    )
