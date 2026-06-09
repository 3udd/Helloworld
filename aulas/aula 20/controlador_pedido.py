from fastapi import APIRouter
from _pedido import Pedido
from sqlalchemy import create_engine, text

router = APIRouter(prefix="/pedidos", tags=["pedidos"])

#inserção no banco "postgresql://'usuario':'senha'@'servidor':'porta'/'banco'"
DATABASE_URL = "postgresql://postgres:123@localhost:5432/lojinha"

@router.post("/")
def cadastrar(pedido: Pedido):

    engine = create_engine(DATABASE_URL)

    try:
        with engine.begin() as con:
            sql = f"""INSERT INTO public.pedidos(
                        cliente_id, data_pedido, status)
                        VALUES (:cliente_id, :data_pedido, :status);"""
            
            dados = {
                "cliente_id" : pedido.cliente_id, 
                "data_pedido": pedido.data_pedido,
                "status": pedido.status
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
                    SELECT id, cliente_id, data_pedido, status FROM pedidos 
                    WHERE id = :id
                  """
            dados = {
                "id": id
            }

            resultado = con.execute(text(sql), dados)
            pedido = resultado.fetchone()

            return pedido._mapping 
            
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
                    SELECT id, cliente_id, data_pedido, status FROM pedidos
                  """
            resultado = con.execute(text(sql))
           
            linhas_do_banco = resultado.fetchall() #Agora pegar todos

            pedidos = []

            for row in linhas_do_banco:
                linha = row._mapping
                pedido = {
                    "id": linha['id'],
                    "cliente_id": linha['cliente_id'],
                    "data_pedido": linha['data_pedido'],
                    "status": linha['status'] 
                }
                pedidos.append(pedido)
            return pedido
            
    except Exception as e:
        return f"erro no banco {e}"

    return []


@router.put('/')
def atualizar(pedido: Pedido):
    #lógica do update
    return True


@router.delete("/")
def deletar(id: int):
    return True
