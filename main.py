from fastapi import FastAPI
from routes.users import user
from routes.materials import material
from routes.prestamos import prestamo
from config.db import Base, engine

app = FastAPI(
    title="Prestamos S.A de C.V",
    description="Api de prueba para almacenar registros de prestamos de material educativo")

# Crear todas las tablas
Base.metadata.create_all(bind=engine)

app.include_router(user)
app.include_router(material)
app.include_router(prestamo)