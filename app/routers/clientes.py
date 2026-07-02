from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session, select

from app.database import get_session
from app.models.clientes import Cliente, ClienteCrear

router_clientes = APIRouter(
    prefix="/clientes",
    tags=["Clientes"]
)


# LISTAR CLIENTES
@router_clientes.get("/", response_model=list[Cliente])
def listar_clientes(session: Session = Depends(get_session)):
    return session.exec(select(Cliente)).all()


# OBTENER CLIENTE
@router_clientes.get("/{id}", response_model=Cliente)
def obtener_cliente(id: int, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )

    return cliente


# CREAR CLIENTE
@router_clientes.post(
    "/",
    response_model=Cliente,
    status_code=status.HTTP_201_CREATED
)
def crear_cliente(cliente: ClienteCrear, session: Session = Depends(get_session)):
    nuevo_cliente = Cliente.model_validate(cliente)

    session.add(nuevo_cliente)
    session.commit()
    session.refresh(nuevo_cliente)

    return nuevo_cliente


# ACTUALIZAR CLIENTE
@router_clientes.put("/{id}", response_model=Cliente)
def actualizar_cliente(
    id: int,
    datos: ClienteCrear,
    session: Session = Depends(get_session)
):
    cliente = session.get(Cliente, id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )

    cliente.nombre = datos.nombre
    cliente.edad = datos.edad
    cliente.descripcion = datos.descripcion

    session.add(cliente)
    session.commit()
    session.refresh(cliente)

    return cliente


# ELIMINAR CLIENTE
@router_clientes.delete("/{id}")
def eliminar_cliente(id: int, session: Session = Depends(get_session)):
    cliente = session.get(Cliente, id)

    if not cliente:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Cliente no encontrado"
        )

    session.delete(cliente)
    session.commit()

    return {"mensaje": "Cliente eliminado correctamente"}