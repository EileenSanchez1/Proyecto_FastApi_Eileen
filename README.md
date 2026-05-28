# API Clientes FastAPI

Proyecto CRUD desarrollado con FastAPI para la gestión de clientes, facturas y transacciones.

---

# Información del Proyecto

- Nombre: Eileen Stefany Sánchez Galindo
- Ficha SENA: 3407184
- Programa: Análisis y Desarrollo de Software (ADSO)

---

# Tecnologías Utilizadas

Este proyecto fue desarrollado utilizando las siguientes tecnologías:

- Python
- FastAPI
- Pydantic
- Uvicorn

---

# Estructura del Proyecto

```bash
PROYECTO_FASTAPI/
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
│   └── main.py
│
├── venv/
├── requirements.txt
├── .gitignore
└── README.md
```

---

# Instalación del Proyecto

## 1. Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
```

---

## 2. Ingresar a la carpeta del proyecto

```bash
cd PROYECTO_FASTAPI
```

---

## 3. Crear entorno virtual

```bash
python -m venv venv
```

---

## 4. Activar entorno virtual

### Windows

```bash
venv\Scripts\activate
```

### Linux o Mac

```bash
source venv/bin/activate
```

---

## 5. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no tienes configurado el archivo requirements.txt puedes instalar manualmente:

```bash
pip install fastapi uvicorn
```

---

# Ejecución del Proyecto

## Opción 1: Ejecutar con Uvicorn

Desde la raíz del proyecto ejecutar:

```bash
uvicorn app.main:app --reload
```

El servidor iniciará en:

```bash
http://127.0.0.1:8000
```

---

## Opción 2: Ejecutar directamente con Python

También puedes iniciar el proyecto ejecutando:

```bash
python app/main.py
```

Para que esta opción funcione correctamente, el archivo `main.py` debe contener:

```python
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(
        "app.main:app",
        host="127.0.0.1",
        port=8000,
        reload=True
    )
```

---

# Documentación Automática

FastAPI genera documentación automática para probar los endpoints de la API.

## Swagger UI

```bash
http://127.0.0.1:8000/docs
```

## ReDoc

```bash
http://127.0.0.1:8000/redoc
```

---

# Funcionalidades del Proyecto

El sistema permite:

- Crear clientes
- Consultar clientes
- Actualizar clientes
- Eliminar clientes
- Gestionar facturas
- Registrar transacciones
- Validar datos utilizando Pydantic
- Consumir endpoints REST

---

# Dependencias Principales

```txt
fastapi
uvicorn
pydantic
```
