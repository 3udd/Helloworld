import uvicorn
from fastapi import FastAPI

app = FastAPI()

#variavel global
dados = {} #fora da funcao

@app.get("/usuario")
def cadastrar(nome:str, senha:str, email:str):
    global dados
    usuario = {}
    usuario['nome'] = nome
    usuario['senha'] = senha
    usuario['email'] = email

    dados[email] = usuario

    return usuario

@app.get("/usuarios")
def todos():
    return dados


if __name__ == "__main__":
    uvicorn.run(
        "usuario:app",
        port = 80,
        reload = True
    )