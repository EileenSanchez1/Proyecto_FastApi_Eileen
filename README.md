# API Gestión de Facturas - FastAPI

Proyecto CRUD desarrollado con **FastAPI**, **SQLModel** y **SQLite** para la gestión de clientes, facturas y transacciones.

---

# Información del Proyecto

- **Nombre:** Eileen Stefany Sánchez Galindo
- **Ficha SENA:** 3407184
- **Programa:** Análisis y Desarrollo de Software (ADSO)

---

# Tecnologías Utilizadas

Este proyecto fue desarrollado utilizando las siguientes tecnologías:

- Python 3
- FastAPI
- SQLModel
- SQLite
- SQLAlchemy
- Pydantic
- Uvicorn

---

# Estructura del Proyecto

```bash
PROYECTO_FASTAPI_EILEEN/
│
├── app/
│   ├── models/
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── routers/
│   │   ├── clientes.py
│   │   ├── facturas.py
│   │   └── transacciones.py
│   │
│   ├── database.py
│   ├── app.py
│   └── __init__.py
│
├── base_datos.db
├── requirements.txt
├── README.md
├── .gitignore
└── venv/
```

---

# Instalación del Proyecto

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

## 2. Ingresar al proyecto

```bash
cd PROYECTO_FASTAPI_EILEEN
```

## 3. Crear el entorno virtual

```bash
python -m venv venv
```

## 4. Activar el entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si es necesario instalar manualmente:

```bash
pip install fastapi uvicorn sqlmodel sqlalchemy pydantic
```

---

# Ejecución del Proyecto

Desde la raíz del proyecto ejecutar:

```bash
uvicorn app.app:app --reload
```

El servidor iniciará en:

```text
http://127.0.0.1:8000
```

---

# Documentación Automática

FastAPI genera automáticamente la documentación de la API.

## Swagger UI

```text
http://127.0.0.1:8000/docs
```

## ReDoc

```text
http://127.0.0.1:8000/redoc
```

---

# Base de Datos

El proyecto utiliza **SQLite** como sistema gestor de base de datos mediante **SQLModel**.

Al iniciar la aplicación se crea automáticamente el archivo:

```text
base_datos.db
```

Las tablas creadas son:

- clientes
- facturas
- transacciones

Las relaciones implementadas son:

- Una factura pertenece a un cliente.
- Una transacción pertenece a una factura.

---

# Funcionalidades

La API permite realizar operaciones CRUD para:

## Clientes

- Crear clientes
- Consultar clientes
- Actualizar clientes
- Eliminar clientes

## Facturas

- Crear facturas
- Consultar facturas
- Actualizar facturas
- Eliminar facturas

## Transacciones

- Crear transacciones
- Consultar transacciones
- Actualizar transacciones
- Eliminar transacciones

---

# Endpoints

## Clientes

```
GET    /clientes
POST   /clientes
GET    /clientes/{id}
PUT    /clientes/{id}
DELETE /clientes/{id}
```

## Facturas

```
GET    /facturas
POST   /facturas
GET    /facturas/{id}
PUT    /facturas/{id}
DELETE /facturas/{id}
```

## Transacciones

```
GET    /transacciones
POST   /transacciones
GET    /transacciones/{id}
PUT    /transacciones/{id}
DELETE /transacciones/{id}
```

---

# Dependencias Principales

```txt
fastapi
uvicorn
sqlmodel
sqlalchemy
pydantic
sqlite3
```

---

# Autor

**Eileen Stefany Sánchez Galindo**

Proyecto FastAPI **Análisis y Desarrollo de Software (ADSO)** del **SENA**.