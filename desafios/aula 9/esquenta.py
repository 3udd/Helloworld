import uvicorn
from fastapi import FastAPI

app = FastAPI()

dados = {}

@app.get("/usuario")
def cadastro(nome, idade:int, email, cidade):
    global dados

    usuario = {
        'nome': nome,
        'idade': idade,
        'email': email,
        'cidade': cidade
    }

    dados[email] = usuario
    return usuario


@app.get("/perfil/{email}")
def mostra_usuario(email):
    return dados[email]


@app.get("/todos")
def mostrar():
    return dados

if __name__ == "__main__":
    uvicorn.run(
        "esquenta:app",
        port = 80,
        reload = True
    )