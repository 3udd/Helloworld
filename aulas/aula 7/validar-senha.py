import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/valida-senha")
def validador(senha:str):
    larg = len(senha)
    validacoes = []

    if 6 < larg < 10:
        validacoes.append("Tamanho válido")
    else:
        validacoes.append("Tamanho inválido")

    if senha.count('%') >= 1:
        validacoes.append("Senha possui %")
    else:
        validacoes.append("Senha não possui %")

    if senha.count('#') >= 1:
        validacoes.append("Senha possui #")
    else:
        validacoes.append("Senha não possui #")

    if senha.count('$') >= 1:
        validacoes.append("Senha possui $")
    else:
        validacoes.append("Senha não possui $")

        return validacoes


if __name__ == "__main__":
    uvicorn.run(
        "validar-senha:app",
        port = 80,
        reload = True
    )