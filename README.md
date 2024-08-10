# FastAPI User Authentication API

Este proyecto es una API para registrar y autenticar usuarios utilizando FastAPI, PostgreSQL, Docker y JWT para la autorización.


## Requisitos

- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/) (para correr los servicios en contenedores)
- [PostgreSQL](https://www.postgresql.org/) (se configura automáticamente con Docker)

## Instalación

### 1. Clona el Repositorio

```bash
git clone https://github.com/diegovaldesjr/fastapi-user-authentication-api.git
cd fastapi-user-authentication-api
```

### 2. Configuración

### Configuración del Entorno

Crea un archivo `.env` en la raíz del proyecto, aquí un ejemplo:

```
SECRET_KEY=your_secret_key
DATABASE_URL=your_url
```

### 3. Uso

### Construir y Ejecutar Contenedores

Construye y ejecuta los contenedores Docker con Docker Compose:

```bash
docker-compose up --build
```

Esto levantará los siguientes servicios:

- **API** en `http://localhost:8000`
- **PostgreSQL** en `http://localhost:5432`

## Endpoints de la API

### Clientes

- **POST** `/register`
    
    Crea un nuevo usuario.
    
- **POST** `/login`
    
    Autentica un usuario y devuelve un token JWT.