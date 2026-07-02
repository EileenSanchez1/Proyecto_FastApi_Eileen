from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class Factura(SQLModel, table=True):
    __tablename__ = "facturas"

    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: Optional[datetime] = Field(default_factory=datetime.now)
    cliente_id: int = Field(foreign_key="clientes.id")

    @property
    def valor_total(self) -> float:
        return 0