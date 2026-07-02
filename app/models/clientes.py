from typing import Optional
from sqlmodel import SQLModel, Field


# Modelo para crear un cliente
class ClienteCrear(SQLModel):
    nombre: str
    edad: int
    descripcion: Optional[str] = None


# Modelo de la tabla clientes
class Cliente(ClienteCrear, table=True):
    __tablename__ = "clientes"

    id: Optional[int] = Field(default=None, primary_key=True)