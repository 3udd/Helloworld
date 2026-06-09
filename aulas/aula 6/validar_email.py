import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/validar-email")
def validar(email:str):
    validacoes = []
    email = email.strip()
    if email.count("@") == 1:
        partes = email.split("@")
    
        if len(partes) == 2:
            print (partes[0])
            print (partes[1])

            if len(partes[0]) < 1:
                validacoes.append("Erro: Não tem nada antes do @") 
            if len(partes[1]) < 1:
                validacoes.append("Erro: Não tem nada depois do @") 

            dominio = partes[1].split(".")

            if len(dominio) > 1:
                if len(dominio[0]) < 1:
                    validacoes.append("Ponto não pode ser seguido do arroba") 
                if len(dominio[1]) < 1:
                    validacoes.append("Tem que haver algo depois do ponto")
                if partes[1].endswith("."):
                    validacoes.append("Não pode terminar com ponto") 
                else:
                    return email
            else:
                validacoes.append("Não parte do domínio precisa ter duas partes separadas por ponto")
    else:
        validacoes.append("O email deve conter um arroba")

    if len(validacoes) == 0:
        return f"email válido. {email}"
    else:
        return validacoes


if __name__ == "__main__":
    uvicorn.run(
        "validar_email:app",
        port = 80,
        reload = True
    )