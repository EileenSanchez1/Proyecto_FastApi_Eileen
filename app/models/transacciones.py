from typing import Optional
from sqlmodel import SQLModel, Field


# Modelo para crear una transacción
class TransaccionCrear(SQLModel):
    valor_unitario: float
    cantidad: int
    factura_id: int


# Modelo de la tabla transacciones
class Transaccion(TransaccionCrear, table=True):
    __tablename__ = "transacciones"

    id: Optional[int] = Field(default=None, primary_key=True)