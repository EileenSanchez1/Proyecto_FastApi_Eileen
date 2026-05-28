from fastapi import APIRouter, HTTPException
from app.models.transacciones import Transaccion, TransaccionCrear
from app.database import lista_transacciones

router_transacciones = APIRouter()

# VER TODAS LAS TRANSACCIONES
@router_transacciones.get("/transacciones")
def listar_transacciones():
    return lista_transacciones

# VER UNA TRANSACCIÓN
@router_transacciones.get("/transacciones/{id}")
def obtener_transaccion(id: int):
    for t in lista_transacciones:
        if t.id == id:
            return t
    raise HTTPException(status_code=404, detail="Transacción no encontrada")

# CREAR TRANSACCIÓN
@router_transacciones.post("/transacciones")
def crear_transaccion(transaccion: Transaccion):
    lista_transacciones.append(transaccion)
    return {"mensaje": "Transacción creada", "transaccion": transaccion}

# EDITAR TRANSACCIÓN (PUT)
@router_transacciones.put("/transacciones/{id}")
def editar_transaccion(id: int, datos_actualizados: TransaccionCrear):
    for t in lista_transacciones:
        if t.id == id:
            t.valor_unitario = datos_actualizados.valor_unitario
            t.cantidad = datos_actualizados.cantidad
            t.factura_id = datos_actualizados.factura_id
            return {"mensaje": "Transacción actualizada", "transaccion": t}
    raise HTTPException(status_code=404, detail="Transacción no encontrada")

# ELIMINAR TRANSACCIÓN (DELETE)
@router_transacciones.delete("/transacciones/{id}")
def eliminar_transaccion(id: int):
    for index, t in enumerate(lista_transacciones):
        if t.id == id:
            lista_transacciones.pop(index)
            return {"mensaje": "Transacción eliminada"}
    raise HTTPException(status_code=404, detail="Transacción no encontrada")