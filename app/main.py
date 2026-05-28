from fastapi import FastAPI

from app.routers.clientes import router_clientes
from app.routers.facturas import router_facturas
from app.routers.transacciones import router_transacciones

app = FastAPI()


@app.get("/")
def root():
    return {"mensaje": "API de Gestion de Facturas Funcionando Correctamente"}


# ROUTERS
app.include_router(router_clientes)
app.include_router(router_facturas)
app.include_router(router_transacciones)