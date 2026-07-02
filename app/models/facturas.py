from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


# Modelo para crear una factura
class FacturaCrear(SQLModel):
    cliente_id: int


# Modelo de la tabla facturas
class Factura(FacturaCrear, table=True):
    __tablename__ = "facturas"

    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: Optional[datetime] = Field(default_factory=datetime.now)

    @property
    def valor_total(self) -> float:
        return 0