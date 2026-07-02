from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models.facturas import Factura

router_facturas = APIRouter(
    prefix="/facturas",
    tags=["Facturas"]
)


# LISTAR FACTURAS
@router_facturas.get("/", response_model=list[Factura])
def listar_facturas(session: Session = Depends(get_session)):
    return session.exec(select(Factura)).all()


# OBTENER FACTURA
@router_facturas.get("/{id}", response_model=Factura)
def obtener_factura(id: int, session: Session = Depends(get_session)):
    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    return factura


# CREAR FACTURA
@router_facturas.post("/", response_model=Factura)
def crear_factura(factura: Factura, session: Session = Depends(get_session)):
    session.add(factura)
    session.commit()
    session.refresh(factura)
    return factura


# ACTUALIZAR FACTURA
@router_facturas.put("/{id}", response_model=Factura)
def actualizar_factura(id: int, datos: Factura, session: Session = Depends(get_session)):
    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    factura.fecha = datos.fecha
    factura.cliente_id = datos.cliente_id

    session.add(factura)
    session.commit()
    session.refresh(factura)

    return factura


# ELIMINAR FACTURA
@router_facturas.delete("/{id}")
def eliminar_factura(id: int, session: Session = Depends(get_session)):
    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(status_code=404, detail="Factura no encontrada")

    session.delete(factura)
    session.commit()

    return {"mensaje": "Factura eliminada correctamente"}