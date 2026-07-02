from typing import Optional
from sqlmodel import SQLModel, Field


class Cliente(SQLModel, table=True):
    __tablename__ = "clientes"

    id: Optional[int] = Field(default=None, primary_key=True)
    nombre: str
    edad: int
    descripcion: Optional[str] = None