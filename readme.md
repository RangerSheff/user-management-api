# User Management API

![CI](https://github.com/RangerSheff/user-management-api/actions/workflows/ci.yml/badge.svg)
![Python](https://img.shields.io/badge/python-3.13-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-REST_API-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-blue)
![Docker](https://img.shields.io/badge/Docker-Containerization-2496ED)
![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

API REST orientada a empresas, desarrollada con FastAPI, PostgreSQL, Docker y prácticas DevSecOps.

## Descripción General

User Management API es un servicio backend RESTful desarrollado con FastAPI y PostgreSQL siguiendo buenas prácticas de arquitectura enterprise, separación de responsabilidades y principios inspirados en Clean Architecture.

Este proyecto fue desarrollado como parte de un desafío técnico para una posición Full Stack Senior y demuestra:

* Desarrollo de APIs REST
* Operaciones CRUD completas
* Arquitectura en capas
* Repository Pattern y Service Layer
* DTOs y validaciones con Pydantic
* Contenerización con Docker
* Testing automatizado
* Logging y middleware
* Estrategia GitFlow
* Separación de ambientes
* Buenas prácticas de seguridad
* Integración CI/CD
* Validaciones automáticas de calidad y seguridad
* Preparación para despliegue en Google Cloud Run

---

## Arquitectura

El proyecto sigue una arquitectura modular basada en capas.

```text
Client
  ↓
FastAPI Router
  ↓
Service Layer
  ↓
Repository Layer
  ↓
SQLAlchemy ORM
  ↓
PostgreSQL
```

### Estructura principal

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

tests/              # Tests unitarios e integración
scripts/            # Automatización local
.github/            # Workflows, Dependabot y governance
```

---

## Stack Tecnológico

| Tecnología     | Propósito                  |
| -------------- | -------------------------- |
| FastAPI        | Framework API REST         |
| PostgreSQL     | Base de datos relacional   |
| SQLAlchemy     | ORM                        |
| Pydantic       | Validación de datos        |
| Docker         | Contenerización            |
| Docker Compose | Orquestación contenedores  |
| Pytest         | Testing automatizado       |
| Ruff           | Linting y calidad código   |
| Bandit         | Security scanning          |
| pip-audit      | Auditoría dependencias     |
| GitHub Actions | Integración continua       |
| Dependabot     | Monitoreo de dependencias  |
| Uvicorn        | Servidor ASGI              |

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
* Validación de roles permitidos
* Control de errores 404 y 409

### Seguridad

* Variables de entorno para información sensible
* Eliminación de credenciales hardcodeadas
* Protección base contra SQL Injection mediante ORM
* Limpieza segura de datos de testing
* Bloqueo de ejecución de tests en ambiente productivo
* Security scanning con Bandit
* Auditoría de dependencias con pip-audit

### Observabilidad

* Middleware de logging HTTP
* Logs estructurados
* Medición de tiempos de respuesta
* Health check básico

---

## Endpoints Disponibles

| Método | Endpoint         | Descripción            |
| ------ | ---------------- | ---------------------- |
| GET    | `/health`        | Health check           |
| GET    | `/users`         | Obtener usuarios       |
| POST   | `/users`         | Crear usuario          |
| GET    | `/users/{user_id}` | Obtener usuario por ID |
| PATCH  | `/users/{user_id}` | Actualizar usuario     |
| DELETE | `/users/{user_id}` | Eliminar usuario       |

---

## Modelo de Usuario

```json
{
  "id": "uuid",
  "username": "string",
  "email": "string",
  "first_name": "string",
  "last_name": "string",
  "role": "admin | user | guest",
  "active": true,
  "created_at": "datetime",
  "updated_at": "datetime"
}
```

---

## Ejemplos de Consumo API

> Base URL local: `http://127.0.0.1:8000`

### Health Check

```bash
curl -X GET http://127.0.0.1:8000/health
```

Respuesta esperada:

```json
{
  "status": "OK"
}
```

---

### Crear Usuario

```bash
curl -X POST http://127.0.0.1:8000/users \
  -H "Content-Type: application/json" \
  -d '{
    "username": "userTestDev",
    "email": "userTestDev@example.com",
    "first_name": "Test",
    "last_name": "Developer",
    "role": "user"
  }'
```

Respuesta esperada:

```json
{
  "id": "generated-uuid",
  "username": "userTestDev",
  "email": "userTestDev@example.com",
  "first_name": "Test",
  "last_name": "Developer",
  "role": "user",
  "active": true,
  "created_at": "2026-01-01T00:00:00",
  "updated_at": "2026-01-01T00:00:00"
}
```

---

### Obtener Usuarios

```bash
curl -X GET http://127.0.0.1:8000/users
```

Respuesta esperada:

```json
[
  {
    "id": "generated-uuid",
    "username": "userTestDev",
    "email": "userTestDev@example.com",
    "first_name": "Test",
    "last_name": "Developer",
    "role": "user",
    "active": true,
    "created_at": "2026-01-01T00:00:00",
    "updated_at": "2026-01-01T00:00:00"
  }
]
```

---

### Obtener Usuario por ID

```bash
curl -X GET http://127.0.0.1:8000/users/{user_id}
```

Ejemplo:

```bash
curl -X GET http://127.0.0.1:8000/users/00000000-0000-0000-0000-000000000000
```

---

### Actualizar Usuario

```bash
curl -X PATCH http://127.0.0.1:8000/users/{user_id} \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "Updated",
    "role": "admin"
  }'
```

---

### Eliminar Usuario

```bash
curl -X DELETE http://127.0.0.1:8000/users/{user_id}
```

Respuesta esperada:

```text
204 No Content
```

---

### Casos de error esperados

#### Usuario no encontrado

```json
{
  "detail": "User not found"
}
```

#### Email duplicado

```json
{
  "detail": "Email already exists"
}
```

#### Username duplicado

```json
{
  "detail": "Username already exists"
}
```

---

## Configuración Local

### Requisitos

* Python 3.11+
* Docker Desktop
* PostgreSQL
* Git

---

## Variables de Entorno

Crear un archivo `.env` basado en `.env.example`:

```bash
cp .env.example .env
```

Ejemplo:

```env
APP_ENV=dev
LOG_LEVEL=INFO

POSTGRES_USER=your_postgres_user
POSTGRES_PASSWORD=your_secure_password
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=user_management_db
```

> No se deben versionar credenciales reales. El archivo `.env` debe permanecer fuera del repositorio.

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

### Levantar reconstruyendo la imagen

```bash
docker compose up --build
```

### Detener infraestructura

```bash
docker compose down
```

### Detener y limpiar volumen de base de datos

```bash
docker compose down -v
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

### Ejecutar tests mostrando líneas faltantes

```bash
pytest --cov=app --cov-report=term-missing
```

---

## Validaciones Locales

Antes de crear un Pull Request se recomienda ejecutar:

```bash
./scripts/validate.sh
```

Este script ejecuta automáticamente:

* Ruff
* Bandit
* pip-audit
* Pytest con coverage

---

## Integración Continua (CI/CD)

El proyecto incluye un pipeline automatizado mediante GitHub Actions.

### Validaciones automáticas

Cada Pull Request ejecuta:

* Linting de código
* Security scanning
* Auditoría de dependencias
* Tests automatizados
* Validación de coverage

### Herramientas utilizadas

| Herramienta | Propósito                    |
| ----------- | ---------------------------- |
| Ruff        | Calidad y estilo código      |
| Bandit      | Seguridad estática Python    |
| pip-audit   | Vulnerabilidades paquetes    |
| Pytest      | Validación funcional         |
| Dependabot  | Actualización dependencias   |

---

## Despliegue en Google Cloud Platform (GCP)

El proyecto incluye un archivo `cloudbuild.yaml` preparado para integraciones CI/CD y despliegue automatizado en Google Cloud Run.

### Objetivos del pipeline

El pipeline automatiza:

* Instalación de dependencias
* Ejecución de tests automatizados
* Construcción de imagen Docker
* Push de imagen a Google Container Registry
* Despliegue automatizado a Cloud Run

### Variables reemplazables

| Variable | Descripción |
| -------- | ----------- |
| PROJECT_ID | ID del proyecto GCP |
| _REGION | Región Cloud Run |
| _SERVICE_NAME | Nombre servicio |
| _IMAGE_NAME | Nombre imagen Docker |

### Región por defecto

El template utiliza:

```text
southamerica-west1
```

Debido a:

* Cercanía geográfica con Chile
* Menor latencia regional
* Compatibilidad con arquitecturas enterprise LATAM

### Ejecución Cloud Build

```bash
gcloud builds submit \
  --config cloudbuild.yaml \
  --substitutions=_REGION=southamerica-west1,_SERVICE_NAME=user-management-api,_IMAGE_NAME=user-management-api
```

### Consideraciones de Producción

Para ambientes reales se recomienda:

* Google Secret Manager
* Cloud SQL PostgreSQL
* IAM mínimo privilegio
* Variables sensibles externas
* Logging y métricas centralizadas
* Observabilidad avanzada

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
* Ramas feature eliminadas después del merge

---

## Repository Governance

El repositorio incluye:

* CODEOWNERS
* Branch protection rules
* Pull Request validation flow
* Dependabot dependency monitoring
* CI quality gates

---

## Consideraciones de Seguridad

* Variables de entorno para información sensible
* Eliminación de credenciales hardcodeadas
* Protección base contra SQL Injection mediante ORM
* Validación de requests con Pydantic
* Logging estructurado
* Separación de capas
* Acceso a base de datos mediante repositories
* Security scanning automatizado
* Auditoría de dependencias
* Limpieza automática de datos de testing
* Bloqueo de ejecución de tests en producción

---

## Referencia de Entrega Challenge

Ejemplo estructura solicitada para entrega final:

```json
{
  "name": "Carlos Javier López Aguayo",
  "mail": "carloslopezaguayo@gmail.com",
  "github_url": "https://github.com/RangerSheff/user-management-api",
  "api_url": "https://user-management-api-xxxxx-southamerica-west1.a.run.app"
}
```

> `api_url` corresponde a una URL generada automáticamente por Google Cloud Run durante despliegues reales.

---

## Mejoras Futuras

* JWT Authentication
* Role Based Authorization
* Vault / Secret Manager
* Kubernetes/OpenShift
* Rate Limiting
* OpenTelemetry
* Alembic migrations
* Redis caching
* Async SQLAlchemy
* Observabilidad avanzada
* SonarQube integration
* Global exception handler
* Healthcheck con validación de base de datos

---

## Autor

Carlos Javier López Aguayo

GitHub:
https://github.com/RangerSheff

---

## Referencia Challenge

El enunciado original del challenge se encuentra almacenado separadamente en:

```text
CHALLENGE.md
```
