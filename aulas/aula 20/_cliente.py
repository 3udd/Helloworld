from pydantic import BaseModel, EmailStr, Field, field_validator

class Cliente(BaseModel):
    nome: str = Field(min_length=3)
    email: EmailStr
    cidade: str = Field(min_length=3)

    @field_validator("nome")
    def nome_deve_ter_espaco(cls, value: str) -> str:
        if " " not in value:
            raise ValueError("O seu nome deve conter ao menos um espaço.")
        return value