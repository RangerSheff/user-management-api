# User Management API

## Descripción General

User Management API es un servicio backend RESTful desarrollado con FastAPI y PostgreSQL siguiendo buenas prácticas de arquitectura enterprise, separación de responsabilidades y principios inspirados en Clean Architecture.

Este proyecto fue desarrollado como parte de un desafío técnico para una posición Full Stack Senior y demuestra:

* Desarrollo de APIs REST
* Operaciones CRUD
* Arquitectura en capas
* Repository Pattern y Service Layer
* Contenerización con Docker
* Testing automatizado
* Logging y middleware
* Estrategia GitFlow
* Separación de ambientes
* Buenas prácticas de seguridad

---

## Arquitectura

El proyecto sigue una arquitectura modular basada en capas.

```text
app/
├── api/            # Rutas y controladores
├── core/           # Configuración, logging y middleware
├── db/             # Configuración de base de datos
├── models/         # Modelos SQLAlchemy
├── repositories/   # Acceso a datos
├── schemas/        # DTOs y validaciones Pydantic
├── services/       # Reglas de negocio
└── main.py         # Punto de entrada aplicación
```

---

## Stack Tecnológico

| Tecnología     | Propósito                 |
| -------------- | ------------------------- |
| FastAPI        | Framework API REST        |
| PostgreSQL     | Base de datos relacional  |
| SQLAlchemy     | ORM                       |
| Pydantic       | Validación de datos       |
| Docker         | Contenerización           |
| Docker Compose | Orquestación contenedores |
| Pytest         | Testing automatizado      |
| Uvicorn        | Servidor ASGI             |

---

## Funcionalidades

### CRUD de Usuarios

* Crear usuario
* Obtener todos los usuarios
* Obtener usuario por ID
* Actualizar usuario
* Eliminar usuario

### Validaciones

* Validación de email único
* Validación de username único
* Validación de payloads mediante Pydantic

### Logging

* Middleware de logging HTTP
* Logs de aplicación
* Medición de tiempos de respuesta

### Testing

* Tests unitarios e integración
* Cobertura automatizada

---

## Endpoints Disponibles

| Método | Endpoint         | Descripción            |
| ------ | ---------------- | ---------------------- |
| GET    | /health          | Health check           |
| GET    | /users           | Obtener usuarios       |
| POST   | /users           | Crear usuario          |
| GET    | /users/{user_id} | Obtener usuario por ID |
| PATCH  | /users/{user_id} | Actualizar usuario     |
| DELETE | /users/{user_id} | Eliminar usuario       |

---

## Configuración Local

### Requisitos

* Python 3.11+
* Docker Desktop
* PostgreSQL
* Git

---

## Variables de Entorno

Crear un archivo `.env`:

```env
DATABASE_URL=postgresql+psycopg2://postgres:admin123@localhost:5432/user_management_db
```

---

## Ejecución Local

### Instalar dependencias

```bash
pip install -r requirements.txt
```

### Levantar API

```bash
uvicorn app.main:app --reload
```

### Documentación Swagger

```text
http://127.0.0.1:8000/docs
```

---

## Docker

### Construir contenedores

```bash
docker compose build
```

### Levantar infraestructura

```bash
docker compose up
```

### Detener infraestructura

```bash
docker compose down
```

---

## Testing Automatizado

### Ejecutar tests

```bash
pytest
```

### Ejecutar tests con coverage

```bash
pytest --cov=app
```

---

## Estrategia GitFlow

El repositorio implementa una estrategia GitFlow simplificada.

### Ramas principales

| Rama    | Propósito              |
| ------- | ---------------------- |
| main    | Producción             |
| quality | Validación QA          |
| develop | Integración desarrollo |

### Flujo de trabajo

```text
feature/* → develop → quality → main
```

### Reglas

* No se permiten pushes directos a main
* No se permiten pushes directos a quality
* Pull Requests obligatorios
* Validación previa antes de merge
* Protección de ramas críticas

---

## Consideraciones de Seguridad

* Variables de entorno para información sensible
* Protección base contra SQL Injection mediante ORM
* Validación de requests con Pydantic
* Logging estructurado
* Separación de capas
* Acceso a base de datos mediante repositories

---

## Mejoras Futuras

* JWT Authentication
* Role Based Authorization
* CI/CD completo
* Kubernetes/OpenShift
* Rate Limiting
* OpenTelemetry
* Alembic migrations
* Redis caching
* Async SQLAlchemy

---

## Autor

Carlos Javier López Aguayo

GitHub:
[https://github.com/RangerSheff](https://github.com/RangerSheff)

---

## Referencia Challenge

El enunciado original del challenge será almacenado separadamente en:

```text
CHALLENGE.md
```
