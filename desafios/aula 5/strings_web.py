import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get("/verif-nome")
def verificador(nome:str):
    nomema = nome.upper()
    nomemi = nome.lower()
    nomecap = nome.capitalize()

    return f"Nome maiúsculo: {nomema}   Nome minúsculo: {nomemi}   Nome capitalizado: {nomecap}"


@app.get("/limpa-frase")
def limpador(frase:str):
    frase_limpa = frase.strip()

    return f"Frase limpa: {frase_limpa}"


@app.get("/censurador")
def censurar(frase:str):
    frase = frase.lower()
    frase_cens = frase.replace("porra", "*****")

    return f"Frase censurada: {frase_cens}"


@app.get("/anal-vogais")
def analizador(palavra:str):
    pal_anal = palavra.count("a")

    return f"Quantidade de letras 'a': {pal_anal}"


@app.get("/verif-senha")
def verificar(senha:str):
    largura = len(senha)

    if 6 < largura < 10:
        return "Senha correta"
    else:
        return "A senha deve conter entre 6 e 10 caracteres"


@app.get("/verif-arquivos")
def verificar(arquivo:str):

    if arquivo.endswith(".pdf"):
        return "É um arquivo pdf"

    if arquivo.startswith("relatorio"):
        return "É um relatório"


@app.get("/criador-apelidos")
def criador(nome:str):
    nome_separado = nome.split()
    apelido = "-".join(nome_separado)

    return f"Seu novo apelido: {apelido}"


@app.get("/localiza-palavra")
def localizador(frase:str, pal_chave:str):
    encontrar = frase.find(pal_chave)

    if encontrar == -1:
        return "Palavra não encontrada"
    return "Palavra encontrada"


@app.get("/verif-email")
def verificar(email:str):
    email = email.lower()

    if email.find("@") == -1:
        return "Seu email não tem arroba"
    
    if email.endswith(".com") == False:
        return "Seu email não termina com '.com'"


@app.get("/anal-frase")
def analizador(frase:str):
    frasema = frase.upper()
    conte = frase.count("e")
    frasecens = frase.replace("a", "*").replace("e", "*").replace("i", "*").replace("o", "*").replace("u", "*")
    fraselarg = len(frase)

    return f"Frase em maiúsculo: {frasema}   Frase censurada: {frasecens}   Quantidade de letras 'e': {conte}   Largura da frase: {fraselarg}"

if __name__ == "__main__":
    uvicorn.run(
        "strings_web:app",
        port = 80,
        reload = True
    )