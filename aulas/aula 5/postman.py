import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/formulario")
def form(nome:str, senha:str, email:str, dia_nasc:int, mes_nasc:int, ano_nasc:int):
    
    if nome != str(nome.title()):
        return "Nome inválido."

    if len(senha) < 8:
        return "Senha inválida"
    
    email = str(email.lower())
    if email.count("@") < 1:
        return "Email inválido"

    if dia_nasc < 0 or dia_nasc > 31:
        return "Dia de nascimento inválido"
    
    if mes_nasc < 0 or mes_nasc > 12:
        return "Mês de nascimento inválido"
    
    if ano_nasc < 0 or ano_nasc > 2026:
        return "Ano de nascimento inválido"

    return f"Nome: {nome}   Senha: {senha}   email? {email}   Data de Nascimento: {dia_nasc}/{mes_nasc}/{ano_nasc}"

if __name__ == "__main__":
    uvicorn.run(
        "postman:app",
        port = 80,
        reload = True
    )