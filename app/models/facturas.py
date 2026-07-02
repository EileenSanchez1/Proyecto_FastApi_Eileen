from typing import Optional
from datetime import datetime
from sqlmodel import SQLModel, Field


class Factura(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    fecha: datetime = Field(default_factory=datetime.now)
    cliente_id: int

    @property
    def valor_total(self) -> float:
        return 0