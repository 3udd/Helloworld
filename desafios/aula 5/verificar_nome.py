import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/verif-nome")
def verifnome(nome:str):
    
    return f"Nome maiúsculo: {nome.upper()}   Nome minúsculo: {nome.lower()}   Nome escrito corretamente: {nome.capitalize()}"

@app.get("limpa-frase")
def limpador(frase:str):
    
    return f"Frase limpa: {frase.strip()}"

if __name__ == "__main__":
    uvicorn.run(
        "verificar_nome:app",
        port = 80,
        reload = True
    )