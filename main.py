from fastapi import FastAPI
from routes.materials import material
from routes.users import user
from routes.prestamos import prestamo

app = FastAPI(
    title="Prestamos S.A de C.V",
    description="Api de prueba para almacenar registros de prestamos de material educativo")

app.include_router(user)
app.include_router(material)
app.include_router(prestamo)