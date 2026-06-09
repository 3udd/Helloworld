import uvicorn
from fastapi import FastAPI

app = FastAPI()

dados = {}

@app.get("/curriculo")
def campos(nome:str, idade:int, sal:float, arquivo:str, id_curriculo:int):
    global dados
    curriculo = {}
    validacoes = []

    if len(nome) < 3:
        validacoes.append("O nome deve ter mais de 3 letras")
    
    if idade < 18 or idade > 65:
        validacoes.append("A idade deve estar entre 18 e 65 anos")

    if sal <= 0:
        validacoes.append("O salário pretendido deve ser maior que 0")

    if not arquivo.endswith(".pdf"):
        validacoes.append("O arquivo deve ser um pdf")

    if len(validacoes) > 0:
        return validacoes
    else:
        curriculo['id'] = id_curriculo
        curriculo['nome'] = nome
        curriculo['idade'] = idade
        curriculo['salário'] = sal
        curriculo['arquivo'] = arquivo

        dados[id_curriculo] = curriculo
        return curriculo

@app.get("/regis-produto")
def campos(nome_prod:str, preco, estoque:int, cat:str, id_prod:int):
    global dados
    registro = {}
    validacoes = []

    if nome_prod.strip() == "":
        validacoes.append("O nome do produto não pode ser vazio")

    preco = float(preco.replace(",", "."))
    if preco <= 0:
        validacoes.append("O preço deve ser um valor positivo")

    if estoque < 0:
        validacoes.append("A quantidade em estoque não pode ser positiva")

    if cat != "Eletrônicos" and cat != "Alimentos" and cat != "Vestuário":
        validacoes.append("A categoria deve ser exatamente uma destas três: 'Eletrônicos', 'Alimentos' ou 'Vestuário'")

    if len(validacoes) > 0:
        return validacoes
    else:
        registro['id produto'] = id_prod
        registro['nome produto'] = nome_prod
        registro['preço'] = preco
        registro['estoque'] = estoque
        registro['categoria'] = cat

        dados[id_prod] = registro
        return registro


@app.get("/login")
def campos(usuario:str, senha:str, conf_senha:str, email:str):
    global dados
    login = {}
    validacoes = []

    if not 5 < len(usuario) < 15:
        validacoes.append("O nome de usuário deve ter entre 5 e 15 caracteres")

    if senha < 8:
        validacoes.append("A senha deve conter pelo menos 8 caracteres")

    if senha != conf_senha:
        validacoes.append("As senhas não coincidem")
    
    if email.count("@") < 1:
        validacoes.append("O email deve conter um arroba")

    if len(validacoes) > 0:
        return validacoes
    else:
        login['email'] = email
        login['usuário'] = usuario
        login['senha'] = senha
        login['confirmação senha'] = conf_senha

        dados[email] = login
        return login


@app.get("/maratona")
def campos(nome_comp:str, distancia:int, cpf:str, tempo:int):
    global dados
    inscricao = {}
    validacoes = []

    if nome_comp.count(" ") < 1:
        validacoes.append("O nome deve ter pelo menos 1 espaço")

    if distancia != 5 and distancia != 10 and distancia != 21 and distancia != 42:
        validacoes.append("A distância deve ser uma das seguintes: 5, 10, 21 ou 42")

    if cpf.isnumeric() == False:
        validacoes.append("O CPF deve conter apenas números")
    else:
        if len(cpf) != 11:
            validacoes.append("O CPF deve ter exatamente 11 dígitos")

    if tempo > 300:
        validacoes.append("O tempo deve ser menor que 300 minutos")

    if len(validacoes) > 0:
        return validacoes
    else:
        inscricao['cpf'] = cpf
        inscricao['nome completo'] = nome_comp
        inscricao['distância'] = distancia
        inscricao['tempo'] = tempo

        dados[cpf] = inscricao
        return inscricao


@app.get("/blog")
def campos(titulo:str, conteudo:str, autor:str, tags:str, id_postagem:int):
    global dados
    postagem = {}
    validacoes = []

    if not 10 < len(titulo) < 100:
        validacoes.append("O título deve ter entre 10 e 100 caracteres")

    if len(conteudo) < 200:
        validacoes.append("O conteúdo deve ter no mínimo 200 caracteres")

    if any(char.isdigit() for char in autor):
        validacoes.append("O nome do autor não pode conter números")

    quant_tags = tags.split()
    if not 1 <= len(quant_tags) <= 5:
        validacoes.append("A quantidade de tags deve estar entre 1 e 5")
        
    if len(validacoes) > 0:
        return validacoes
    else:
        postagem['id postagem'] = id_postagem
        postagem['título'] = titulo
        postagem['conteúdo'] = conteudo
        postagem['autor'] = autor
        postagem['tags'] = tags

        dados[id_postagem] = postagem
        return postagem


@app.get("/dados")
def todos():
    return dados


if __name__ == "__main__":
    uvicorn.run(
        "reforco_json:app",
        port = 80,
        reload = True
    )