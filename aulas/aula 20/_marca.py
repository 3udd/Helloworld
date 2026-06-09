from pydantic import BaseModel, Field

class Marca(BaseModel):
    nome: str = Field(min_length=3)
    pais: str