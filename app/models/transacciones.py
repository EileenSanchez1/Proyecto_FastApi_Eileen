from typing import Optional
from sqlmodel import SQLModel, Field


class Transaccion(SQLModel, table=True):
    __tablename__ = "transacciones"

    id: Optional[int] = Field(default=None, primary_key=True)
    valor_unitario: float
    cantidad: int
    factura_id: int = Field(foreign_key="facturas.id")