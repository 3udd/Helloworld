import uvicorn
from fastapi import FastAPI

app = FastAPI()



@app.get("/rpg/{pontos}")
def pontuacao(pontos:int):

    if pontos > 1000:
        return ("Você é uma lenda viva!")
    elif pontos > 500:
        return ("Você é um mestre da aventura!")
    elif pontos > 100:
        return ("Você é um aventureiro experiente!")
    else:
        return ("Você é um iniciante!")

@app.get("/class-clima/{temp}")
def temperatura(temp:int):
    if temp > 25:
        return ("Está quente. Use roupas leves.")
    elif temp > 15:
        return ("O clima está agradável, aproveite o dia!")
    else: 
        return ("Está frio, leve um casaco.")

@app.get("/senha/{senha}")
def senhamagica(senha:str):
    if senha == "abracadabra":
        return ("Acesso concedido!")
    else:
        return ("Senha incorreta. Tente novamente.")

@app.get("/idade-filmes/{idade}/{classif}")
def verificador(idade:int, classif:int):

    if idade >= classif:
        return ("Você pode assistir a esse filme.")
    else:
        return ("Você não pode assistir a esse filme.")

@app.get("/validar-idade")
def validar(idade:int):
    if idade > 18:
        return ("Pode ver")
    return ("Não pode ver")

@app.get("/vingador/{poder}/{joia}")
def teste(poder:int, joia:bool):
    if poder > 50 and joia == True:
        return ("Você é o vingador supremo!")
    else:
        return ("Seu poder é insuficiente.")

@app.get("/ano-bissexto/{ano}")
def validarano(ano:int):
    if ano % 4 == 0 or ano % 400 == 0:
        if ano % 100 != 0:
            return ("É um ano bissexto.")
    return ("Não é um ano bissexto.")



if __name__ == "__main__":
    uvicorn.run(
        "desafios_web:app",
        port = 80,
        reload = True
    )