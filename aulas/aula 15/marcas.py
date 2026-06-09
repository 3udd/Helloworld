import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

#inserção no banco "postgresql://'usuario':'senha'@'servidor':'porta'/'banco'"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"

@app.get("/cadastrar")
def cadastrar(nome_marca, pais_origem):

    # try:
    #     #validacao
    # except:
    #     return 'Valor inválido'

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""INSERT INTO public.marcas
                        (nome_marca, pais_origem)
	                VALUES (?, ?);"""
            
            dados = {
                "nomezinho": nome_marca,
                "paisinho": pais_origem
            }

            con.execute(text(sql), dados)
    except Exception as e:
        return e
    engine.dispose()
        

@app.get("/atualizar")
def atualizar(id_marca, nome_marca, pais_origem):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""UPDATE public.marcas
	                    SET nome_marca=:nomezinho, pais_origem=:paisinho
	                WHERE <id = :idzinho>;"""

            dados = {
                "idzinho": id_marca,
                "nomezinho": nome_marca,
                "pais_origem": pais_origem
            }

            con.execute(text(sql), dados)
    except Exception as e:
        return e
    engine.dispose()


@app.get("/buscar/{id}")
def buscar(id: int):
    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""SELECT id_marca, nome_marca, pais_origem FROM marcas
                        WHERE id = :idzinho"""
            
            dados = {
                "idzinho": id
            }

            resultado = con.execute(text(sql), dados)
            marcas = resultado.fetchone()

            return marcas._mapping

    except Exception as e:
        return e
    engine.dispose()


@app.get("/deletar")
def deletar():

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f""""""

            dados = {

            }

            con.execute(text(sql), dados)
    except Exception as e:
        return e
    engine.dispose()
    


if __name__ == '__main__':
    uvicorn.run(
        ':app',
        port=80,
        reload=True
    )