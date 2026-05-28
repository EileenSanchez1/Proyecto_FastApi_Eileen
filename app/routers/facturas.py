from fastapi import APIRouter, HTTPException
from app.models.facturas import Factura, FacturaCrear
from app.database import lista_facturas

router_facturas = APIRouter()

# VER TODAS LAS FACTURAS
@router_facturas.get("/facturas")
def listar_facturas():
    # Devolvemos las facturas incluyendo el valor_total calculado en cada una
    resultado = []
    for f in lista_facturas:
        datos = f.dict()
        datos["valor_total"] = f.valor_total
        resultado.append(datos)
    return resultado

# VER UNA FACTURA
@router_facturas.get("/facturas/{id}")
def obtener_factura(id: int):
    for f in lista_facturas:
        if f.id == id:
            datos = f.dict()
            datos["valor_total"] = f.valor_total
            return datos
    raise HTTPException(status_code=404, detail="Factura no encontrada")

# CREAR FACTURA
@router_facturas.post("/facturas")
def crear_factura(factura: Factura):
    lista_facturas.append(factura)
    return {
        "mensaje": "Factura creada correctamente",
        "factura": factura.dict(),
        "valor_total": factura.valor_total
    }

# EDITAR FACTURA (PUT)
@router_facturas.put("/facturas/{id}")
def editar_factura(id: int, datos_actualizados: FacturaCrear):
    for f in lista_facturas:
        if f.id == id:
            f.fecha = datos_actualizados.fecha
            f.cliente = datos_actualizados.cliente
            f.lista_transacciones = datos_actualizados.lista_transacciones
            return {
                "mensaje": "Factura actualizada",
                "factura": f.dict(),
                "valor_total": f.valor_total
            }
    raise HTTPException(status_code=404, detail="Factura no encontrada")

# ELIMINAR FACTURA (DELETE)
@router_facturas.delete("/facturas/{id}")
def eliminar_factura(id: int):
    for index, f in enumerate(lista_facturas):
        if f.id == id:
            lista_facturas.pop(index)
            return {"mensaje": "Factura eliminada"}
    raise HTTPException(status_code=404, detail="Factura no encontrada")