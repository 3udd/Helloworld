import uvicorn
from fastapi import FastAPI

app = FastAPI()

#variavel global
dados = {} #fora da funcao

@app.get("/usuario")
def cadastrar(nome:str, senha:str, email:str):
    global dados
    usuario = {}
    endereco = []

    usuario = {
        'nome': nome,
        'senha': senha,
        'email': email,
        'endereço': endereco
    }

    dados[email] = usuario

    return usuario

@app.get("/adicionar-endereco")
def ad_endereco(email, rua, numero, cidade, estado):
    global dados

    endereco = {
        'rua': rua,
        'numero': numero,
        'cidade': cidade,
        'estado': estado
    }

    if email in dados:
        usuario = dados[email]
        usuario['endereco'].append(endereco)
        return usuario
    else:
        return "Usuário não encontrado"

@app.get("/usuarios")
def todos():
    return dados


if __name__ == "__main__":
    uvicorn.run(
        "usuario:app",
        port = 80,
        reload = True
    )