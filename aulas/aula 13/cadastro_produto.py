import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

#inserção no banco "postgresql://'usuario':'senha'@'servidor':'porta'/'banco'"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"

@app.get("/cadastrar")
def cadastrar(nome, valor):

    try:
        valor = valor.replace(',', '.')
        valor = float(valor)
    except:
        return 'Valor do produto inválido'

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""INSERT INTO public.produto
                            (nome, valor)
	                VALUES ( :nomezinho, :valorzinho);"""
            
            dados = {
                "nomezinho": nome,
                "valorzinho": valor
            }

            con.execute(text(sql), dados)
    except Exception as e:
        return e
    engine.dispose()
        

@app.get("/atualizar")
def atualizar(id, nome, valor):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""UPDATE public.produto
	                SET nome=:nomezinho, valor=:valorzinho
	                WHERE id = :idzinho;"""

            dados = {
                "idzinho": id,
                "nomezinho": nome,
                "valorzinho": valor
            }

            con.execute(text(sql), dados)
    except Exception as e:
        return e
    engine.dispose()


@app.get("/deletar")
def deletar(id):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""DELETE FROM public.produto
	                    WHERE id = :idzinho;"""

            dados = {
                "idzinho": id
            }

            con.execute(text(sql), dados)
    except Exception as e:
        return e
    engine.dispose()
    


if __name__ == '__main__':
    uvicorn.run(
        'cadastro_produto:app',
        port=80,
        reload=True
    )