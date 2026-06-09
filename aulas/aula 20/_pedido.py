from pydantic import BaseModel, Field

class Pedido(BaseModel):
    cliente_id: int
    data_pedido: str
    status: str