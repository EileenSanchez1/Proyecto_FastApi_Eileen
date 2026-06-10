from fastapi import APIRouter, HTTPException
from app.models.transacciones import Transaccion, TransaccionCrear
from app.database import lista_transacciones

# Configuración del enrutador con prefijo y etiquetas para Swagger
router_transacciones = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)

# VER TODAS LAS TRANSACCIONES
@router_transacciones.get("/")
def listar_transacciones():
    return lista_transacciones

# VER UNA TRANSACCIÓN POR ID
@router_transacciones.get("/{id}")
def obtener_transaccion(id: int):
    for transaccion in lista_transacciones:
        if transaccion.id == id:
            return transaccion
    raise HTTPException(status_code=404, detail="Transacción no encontrada")

# CREAR UNA TRANSACCIÓN
@router_transacciones.post("/")
def crear_transaccion(transaccion: TransaccionCrear):
    nuevo_id = len(lista_transacciones) + 1
    nueva_transaccion = Transaccion(id=nuevo_id, **transaccion.dict())
    lista_transacciones.append(nueva_transaccion)
    return nueva_transaccion

# EDITAR UNA TRANSACCIÓN
@router_transacciones.put("/{id}")
def actualizar_transaccion(id: int, transaccion_actualizada: TransaccionCrear):
    for index, transaccion in enumerate(lista_transacciones):
        if transaccion.id == id:
            lista_transacciones[index] = Transaccion(id=id, **transaccion_actualizada.dict())
            return lista_transacciones[index]
    raise HTTPException(status_code=404, detail="Transacción no encontrada")

# ELIMINAR UNA TRANSACCIÓN
@router_transacciones.delete("/{id}")
def eliminar_transaccion(id: int):
    for index, transaccion in enumerate(lista_transacciones):
        if transaccion.id == id:
            lista_transacciones.pop(index)
            return {"detail": "Transacción eliminada con éxito"}
    raise HTTPException(status_code=404, detail="Transacción no encontrada")