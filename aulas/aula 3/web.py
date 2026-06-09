import uvicorn
from fastapi import FastAPI

app = FastAPI() #criando a app em memória

"""
    Saudação
@app.get("/saudar/{n}")
def nome(n):
    saudacao = f"Seu nome é {n}"
    print (saudacao)
    return saudacao
"""


        #termometro
@app.get("/temperatura/{temp}")
def avaltemp(temp:int):

    if temp >= 35:
        return ("Muito quente.")
    elif temp >= 20:
        return ("Agradável.")
    else:
        return ("Frio.")

        #notas
@app.get("/notas/{nota}")
def avalnota(nota:float):

    if nota >= 7:
        return ("Aprovado.")
    elif nota >= 5:
        return ("Recuperação.")
    else:
        return ("Reprovado.")

        #maior numero
@app.get("/maiormenor/{num1}/{num2}")
def compnums(num1:int, num2:int):

    if num1 > num2:
        return ("O primeiro é maior.")
    elif num2 > num1:
        return ("O segundo é maior.")
    else:
        return ("Ambos são iguais.")

@app.get("/")   #atalho para função, determinado pela rota
def home():
    print ("aaa")   #aparece no terminal
    return 'legau'  #aparece na página

if __name__ == "__main__":  #testa se é execução python
    uvicorn.run(
        "web:app",
        port = 80,
        reload = True
    )