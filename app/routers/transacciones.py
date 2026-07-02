from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session, select

from app.database import get_session
from app.models.transacciones import Transaccion

router_transacciones = APIRouter(
    prefix="/transacciones",
    tags=["Transacciones"]
)


# LISTAR TRANSACCIONES
@router_transacciones.get("/", response_model=list[Transaccion])
def listar_transacciones(session: Session = Depends(get_session)):
    return session.exec(select(Transaccion)).all()


# OBTENER TRANSACCION
@router_transacciones.get("/{id}", response_model=Transaccion)
def obtener_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    return transaccion


# CREAR TRANSACCION
@router_transacciones.post("/", response_model=Transaccion)
def crear_transaccion(transaccion: Transaccion, session: Session = Depends(get_session)):
    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)

    return transaccion


# ACTUALIZAR TRANSACCION
@router_transacciones.put("/{id}", response_model=Transaccion)
def actualizar_transaccion(id: int, datos: Transaccion, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    transaccion.valor_unitario = datos.valor_unitario
    transaccion.cantidad = datos.cantidad
    transaccion.factura_id = datos.factura_id

    session.add(transaccion)
    session.commit()
    session.refresh(transaccion)

    return transaccion


# ELIMINAR TRANSACCION
@router_transacciones.delete("/{id}")
def eliminar_transaccion(id: int, session: Session = Depends(get_session)):
    transaccion = session.get(Transaccion, id)

    if not transaccion:
        raise HTTPException(status_code=404, detail="Transacción no encontrada")

    session.delete(transaccion)
    session.commit()

    return {"mensaje": "Transacción eliminada correctamente"}