from fastapi import APIRouter, HTTPException
from app.models.facturas import Factura, FacturaCrear
from app.database import lista_facturas

# Configuración del enrutador con prefijo y etiquetas para Swagger
router_facturas = APIRouter(
    prefix="/facturas",
    tags=["Facturas"]
)

# VER TODAS LAS FACTURAS
@router_facturas.get("/")
def listar_facturas():
    return lista_facturas

# VER UNA FACTURA POR ID
@router_facturas.get("/{id}")
def obtener_factura(id: int):
    for factura in lista_facturas:
        if factura.id == id:
            return factura
    raise HTTPException(status_code=404, detail="Factura no encontrada")

# CREAR UNA FACTURA
@router_facturas.post("/")
def crear_factura(factura: FacturaCrear):
    nuevo_id = len(lista_facturas) + 1
    nueva_factura = Factura(id=nuevo_id, **factura.dict())
    lista_facturas.append(nueva_factura)
    return nueva_factura

# EDITAR UNA FACTURA
@router_facturas.put("/{id}")
def actualizar_factura(id: int, factura_actualizada: FacturaCrear):
    for index, factura in enumerate(lista_facturas):
        if factura.id == id:
            lista_facturas[index] = Factura(id=id, **factura_actualizada.dict())
            return lista_facturas[index]
    raise HTTPException(status_code=404, detail="Factura no encontrada")

# ELIMINAR UNA FACTURA
@router_facturas.delete("/{id}")
def eliminar_factura(id: int):
    for index, factura in enumerate(lista_facturas):
        if factura.id == id:
            lista_facturas.pop(index)
            return {"detail": "Factura eliminada con éxito"}
    raise HTTPException(status_code=404, detail="Factura no encontrada")