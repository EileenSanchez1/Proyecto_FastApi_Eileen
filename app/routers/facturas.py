from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select
from datetime import datetime

from app.database import get_session
from app.models.facturas import Factura, FacturaCrear
from app.models.clientes import Cliente

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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada"
        )

    return factura


# CREAR FACTURA
@router_facturas.post(
    "/",
    response_model=Factura,
    status_code=status.HTTP_201_CREATED
)
def crear_factura(
    datos: FacturaCrear,
    session: Session = Depends(get_session)
):

    cliente = session.get(Cliente, datos.cliente_id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )

    factura = Factura.model_validate(datos)

    # Dejamos la fecha automática como quedó funcionando
    factura.fecha = datetime.now()

    session.add(factura)
    session.commit()
    session.refresh(factura)

    return factura


# ACTUALIZAR FACTURA
@router_facturas.put("/{id}", response_model=Factura)
def actualizar_factura(
    id: int,
    datos: FacturaCrear,
    session: Session = Depends(get_session)
):

    factura = session.get(Factura, id)

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada"
        )

    cliente = session.get(Cliente, datos.cliente_id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )

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
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada"
        )

    session.delete(factura)
    session.commit()

    return {"mensaje": "Factura eliminada correctamente"}