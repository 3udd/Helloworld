from fastapi import APIRouter
from _marca import Marca
from sqlalchemy import create_engine, text

router = APIRouter(prefix="/marcas", tags=["marcas"])

#inserção no banco "postgresql://'usuario':'senha'@'servidor':'porta'/'banco'"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"

@router.post("/")
def cadastrar(marca: Marca):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""INSERT INTO public.marcas(
                        nome_marca, pais_origem)
                        VALUES (:nome_marca, :pais_origem);"""
            
            dados = {
                "nome_marca" : marca.nome_marca, 
                "pais_origem": marca.pais_origem
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
                    SELECT id, nome_marca, pais_origem FROM marcas
                    WHERE id = :id
                  """
            dados = {
                "id": id
            }

            resultado = con.execute(text(sql), dados)
            marca = resultado.fetchone()

            return marca._mapping 
            
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
                    SELECT id, nome_marca, pais_origem FROM marcas
                  """
            resultado = con.execute(text(sql))
           
            linhas_do_banco = resultado.fetchall() #Agora pegar todos

            marcas = []

            for row in linhas_do_banco:
                linha = row._mapping
                marca = {
                    "id": linha['id'],
                    "nome_marca": linha['nome_marca'],
                    "pais_origem": linha['pais_origem'],
                }
                marcas.append(marca)
            return marca
            
    except Exception as e:
        return f"erro no banco {e}"

    return []


@router.put('/')
def atualizar(marca: Marca):
    #lógica do update
    return True


@router.delete("/")
def deletar(id: int):
    return True
