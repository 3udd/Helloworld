import uvicorn
from fastapi import FastAPI
from sqlalchemy import create_engine, text

app = FastAPI()

#inserção no banco "postgresql://'usuario':'senha'@'servidor':'porta'/'banco'"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"

@app.get("/cadastrar")
def cadastrar():

    # try:
    #     #validacao
    # except:
    #     return 'Valor inválido'

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
        

@app.get("/atualizar")
def atualizar():
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