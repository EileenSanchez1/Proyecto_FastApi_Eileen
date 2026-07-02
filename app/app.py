from fastapi import FastAPI

from app.database import crear_tablas

from app.routers.clientes import router_clientes
from app.routers.facturas import router_facturas
from app.routers.transacciones import router_transacciones

app = FastAPI()


@app.on_event("startup")
def on_startup():
    crear_tablas()


@app.get("/")
def root():
    return {"mensaje": "API de Gestion de Facturas Funcionando Correctamente"}


# ROUTERS
app.include_router(router_clientes)
app.include_router(router_facturas)
app.include_router(router_transacciones)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)