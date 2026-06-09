from fastapi import APIRouter
from _cliente import Cliente
from sqlalchemy import create_engine, text

router = APIRouter(prefix="/clientes", tags=["clientes"])

#inserção no banco "postgresql://'usuario':'senha'@'servidor':'porta'/'banco'"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"

@router.post("/")
def cadastrar(cliente: Cliente):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""INSERT INTO public.clientes(
                        nome_cliente, email, cidade)
                        VALUES (:nome, :email, :cidade);"""
            
            dados = {
                "nome" : cliente.nome, 
                "email": cliente.email,
                "cidade": cliente.cidade
            }

            con.execute(text(sql), dados)
    except Exception as e:
        return e
    engine.dispose()
        

#recovery =>consulta (getOne e getAll => pegar 1 ou pegar todos)
@router.get('/{id}')
def getOne(id: int ):

    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    SELECT id, nome, email, cidade FROM clientes 
                    WHERE id = :id
                  """
            dados = {
                "id": id
            }

            resultado = con.execute(text(sql), dados)
            produto = resultado.fetchone()

            return produto._mapping 
            
    except:
        return "erro no banco"

    return {}


#postman http://localhost/cliente/todos
@router.get('/')
def todos():

    engine = create_engine(DATABASE_URL)
    try:
        with engine.connect() as con:
            sql = """
                    SELECT id, nome, email, cidade FROM clientes 
                  """
            resultado = con.execute(text(sql))
           
            linhas_do_banco = resultado.fetchall() #Agora pegar todos

            clientes = []

            for row in linhas_do_banco:
                linha = row._mapping
                cliente = {
                    "id": linha['id'],
                    "nome": linha['nome'],
                    "email": linha['email'],
                    "cidade": linha['cidade'] 
                }
                clientes.append(cliente)
            return cliente
            
    except Exception as e:
        return f"erro no banco {e}"

    return []


@router.put('/')
def atualizar(cliente: Cliente):
    #lógica do update
    return True


@router.delete("/")
def deletar(id: int):
    return True
