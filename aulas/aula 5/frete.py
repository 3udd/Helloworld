import uvicorn
from fastapi import FastAPI

app = FastAPI()

# sp = 200, rj = 15, qualquer = 25

@app.get("/frete")
def frete(valor, estado:str):
    valorFrete = 25
    estado = estado.lower()
    
    try:
        valor = float(valor.replace(",", "."))
    except:
        return "número inválido"

    if estado == "sp":
        valorFrete = 200
    if estado == "rj":
        valorFrete = 15
    return f"O valor final foi {valor+valorFrete}"


if __name__ == "__main__":
    uvicorn.run(
        "frete:app",
        port = 80,
        reload = True
    )