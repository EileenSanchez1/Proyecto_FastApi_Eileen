from fastapi import APIRouter, HTTPException
from app.models.clientes import Cliente, ClienteCrear
from app.database import lista_clientes

# Configuración del enrutador con prefijo y etiquetas para Swagger
router_clientes = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)

# VER TODOS LOS CLIENTES
@router_clientes.get("/")
def listar_clientes():
    return lista_clientes

# VER UN CLIENTE POR ID
@router_clientes.get("/{id}")
def obtener_cliente(id: int):
    for cliente in lista_clientes:
        if cliente.id == id:
            return cliente
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# CREAR UN CLIENTE
@router_clientes.post("/")
def crear_cliente(cliente: ClienteCrear):
    nuevo_id = len(lista_clientes) + 1
    nuevo_cliente = Cliente(id=nuevo_id, **cliente.dict())
    lista_clientes.append(nuevo_cliente)
    return nuevo_cliente

# EDITAR UN CLIENTE
@router_clientes.put("/{id}")
def actualizar_cliente(id: int, cliente_actualizado: ClienteCrear):
    for index, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes[index] = Cliente(id=id, **cliente_actualizado.dict())
            return lista_clientes[index]
    raise HTTPException(status_code=404, detail="Cliente no encontrado")

# ELIMINAR UN CLIENTE
@router_clientes.delete("/{id}")
def eliminar_cliente(id: int):
    for index, cliente in enumerate(lista_clientes):
        if cliente.id == id:
            lista_clientes.pop(index)
            return {"detail": "Cliente eliminado con éxito"}
    raise HTTPException(status_code=404, detail="Cliente no encontrado")