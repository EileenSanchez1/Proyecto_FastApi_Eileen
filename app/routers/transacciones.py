from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models.transacciones import Transaccion, TransaccionCrear
from app.models.facturas import Factura

router_transacciones = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)


# LISTAR TRANSACCIONES
@router_transacciones.get("/", response_model=list[Transaccion])
def listar_transacciones(session: Session = Depends(get_session)):
    return session.exec(select(Transaccion)).all()


# OBTENER TRANSACCIÓN
@router_transacciones.get("/{id}", response_model=Transaccion)
def obtener_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transacción no encontrada"
        )

    return transaccion


# CREAR TRANSACCIÓN
@router_transacciones.post(
    "/",
    response_model=Transaccion,
    status_code=status.HTTP_201_CREATED
)
def crear_transaccion(
    datos: TransaccionCrear,
    session: Session = Depends(get_session)
):

    factura = session.get(Factura, datos.factura_id)

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada"
        )

    nueva_transaccion = Transaccion.model_validate(datos)

    session.add(nueva_transaccion)
    session.commit()
    session.refresh(nueva_transaccion)

    return nueva_transaccion


# ACTUALIZAR TRANSACCIÓN
@router_transacciones.put("/{id}", response_model=Transaccion)
def actualizar_transaccion(
    id: int,
    datos: TransaccionCrear,
    session: Session = Depends(get_session)
):

    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transacción no encontrada"
        )

    factura = session.get(Factura, datos.factura_id)

    if not factura:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Factura no encontrada"
        )

    transaccion.valor_unitario = datos.valor_unitario
    transaccion.cantidad = datos.cantidad
    transaccion.factura_id = datos.factura_id

    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)

    return transaccion


# ELIMINAR TRANSACCIÓN
@router_transacciones.delete("/{id}")
def eliminar_transaccion(id: int, session: Session = Depends(get_session)):

    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Transacción no encontrada"
        )

    session.delete(transaccion)
    session.commit()

    return {"mensaje": "Transacción eliminada correctamente"}