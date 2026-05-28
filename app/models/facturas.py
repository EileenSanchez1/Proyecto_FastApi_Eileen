from pydantic import BaseModel
from datetime import datetime
from typing import List
from app.models.clientes import Cliente
from app.models.transacciones import Transaccion

class FacturaCrear(BaseModel):
    fecha: datetime = datetime.now()
    cliente: Cliente
    lista_transacciones: List[Transaccion] = []

class Factura(FacturaCrear):
    id: int

    @property
    def valor_total(self) -> float:
        return sum(t.valor_unitario * t.cantidad for t in self.lista_transacciones)