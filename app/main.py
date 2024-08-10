from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.users import endpoints
from app.database import init_db

app = FastAPI()
origins = ['*']

# Inicializar la base de datos
init_db()

app.add_middleware(
    CORSMiddleware, allow_origins=origins, allow_credentials=True, allow_methods=['*'], allow_headers=['*']
)

app.include_router(endpoints.router)
