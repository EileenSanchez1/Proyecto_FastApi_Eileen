from fastapi import FastAPI
from app.database import crear_tablas
from app.routers.clientes import router_clientes
from app.routers.facturas import router_facturas
from app.routers.transacciones import router_transacciones


app = FastAPI(
    title="API Gestión de Facturas",
    description="""
Sistema de gestión de ventas desarrollado con:

- FastAPI
- SQLModel
- SQLite
- Relaciones entre tablas
- Facturas
- Clientes
- Transacciones
- Cálculo automático de totales
""",
    version="1.0.0"
)


# CREAR TABLAS
@app.on_event("startup")
async def startup():
    crear_tablas()



# ENDPOINT PRINCIPAL
@app.get("/")
async def root():
    return {
        "mensaje":
        "API de Gestión de Facturas Funcionando Correctamente"
    }



app.include_router(router_clientes)
app.include_router(router_facturas)
app.include_router(router_transacciones)


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.app:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )