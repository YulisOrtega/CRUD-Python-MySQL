from fastapi import FastAPI
from routes.users import user

app = FastAPI(
    title="Prestamos S.A de C.V",
    description="Api de prueba para almacenar registros de prestamos de material educativo")

app.include_router(user)