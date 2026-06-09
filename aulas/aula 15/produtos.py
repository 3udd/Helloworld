import uvicorn
from fastapi import FastAPI


#pip install sqlalchemy
from sqlalchemy import create_engine, text


app = FastAPI()


#inserção no banco "postgresql://usuario:senha@servidor:porta/banco"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"


@app.get('/cadastrar')
def cadastrar(nomeFront, valor, marca:int):
    # validaçõe regra de negócio
    try:
        valor = valor.replace(',', '.')
        valor = float(valor)
    except:
        return 'Valor do produto inválido'
    
    valorTratado = valor


    #crio a conexao
    engine = create_engine(DATABASE_URL)


    try:
        with engine.begin() as con: #inicializo a transação
            sql = """INSERT INTO public.produto
                                (nome, valor, marca_id)
                        VALUES ( :nomezinho, :valorzinho, :marca_id)"""            
            dados = {
                "nomezinho" : nomeFront,
                "valorzinho": valorTratado,
                "marca_id": marca
            }


            con.execute(text(sql), dados)
    except Exception as e:
        return e
    engine.dispose()


@app.get('/deletar')
def deletar(id:int):
    #crio a conexao
    engine = create_engine(DATABASE_URL)


    try:
        with engine.begin() as con: #inicializo a transação
            sql = """DELETE FROM public.produto
	                    WHERE id = :id"""            
            dados = {
                "id" : id
            }


            con.execute(text(sql), dados)
            return 'Apagado com sucesso'
    except Exception as e:
        return e
    engine.dispose()


@app.get('/atualizar')
def atualizar(id:int, valor, nome = 'xxxxxx'): #valor padrão caso não informado
    #crio a conexao
    engine = create_engine(DATABASE_URL)


    try:
        with engine.begin() as con: #inicializo a transação
            sql = """UPDATE public.produto
	                    SET nome = :nomeNovo, valor=:valorNovo
                        WHERE id=:id
	                """            
            dados = {
                "nomeNovo" : nome,
                "valorNovo" : valor,
                'id': id
            }


            con.execute(text(sql), dados)
            return 'atualizado com sucesso'
    except Exception as e:
        return e
    engine.dispose()


#Read => getOne e getALL
@app.get("/buscar/{id}") #id no REST se chama recurso
def buscar(id: int):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con: # observe que é connect e não begin
                                      # Como é só consulta não preciso de transação
            sql = """
                    SELECT id, nome, valor FROM produto 
                    WHERE id = :id
                  """
            dados = {
                "id": id
            }


            resultado = con.execute(text(sql), dados)
            produto = resultado.fetchone() #puxou apenas a 1ª linha


            return produto._mapping #atalho mas tem problemas 
            
    except:
        return "erro no banco"


@app.get('/listar')
def listar():
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    SELECT id, nome, valor FROM produto 
                  """
            resultado = con.execute(text(sql))
           
            linhas_do_banco = resultado.fetchall() #Agora pegar todos


            produtos = []


            #mais lento mas mais legível
            for row in linhas_do_banco:
                linha = row._mapping #pega as colunas por nome
                #modelo para o Frontend
                produto = {
                    "id": linha['id'],
                    "preco": f"R$ {str(linha['valor']).replace('.', ',')}",
                    "nome": linha['nome'], 
                }
                produtos.append(produto)
            return produtos 
            
    except Exception as e:
        return f"erro no banco {e}"
    
@app.get('/listar-por-pais/{pais}')
def listar_por_pais(pais):
    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = f"""
                    SELECT p.id, p.nome, valor, nome_marca, pais_origem
                    FROM produto p
                    JOIN marca m ON p.marca_id = m.id
                    WHERE m.pais_origem = :paisBanco; 
                  """
      
            dados = {
                'paisBanco': pais
            }

            resultado = con.execute(text(sql), dados)
           
            linhas_do_banco = resultado.fetchall() #Agora pegar todos


            produtos = []


     
            for row in linhas_do_banco:
                linha = row._mapping #pega as colunas por nome
                #modelo para o Frontend
                produto = {
                    "id": linha['id'],
                    "preco": linha['valor'],
                    "nome": linha['nome'],
                    "marca": {
                        "nome": linha['nome_marca'],
                        "pais": linha['pais']
                    }
                }
                produtos.append(produto)


            return produtos 
            
    except:
        return "erro no banco"




#iniciar a aplicação
if __name__ == '__main__':
    uvicorn.run(
        'produtos:app',
        port=80,
        reload=True
    )
