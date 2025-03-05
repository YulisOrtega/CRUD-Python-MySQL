from fastapi import APIRouter, HTTPException, Depends, dependencies, security
from fastapi.security import HTTPBearer
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from auth import create_access_token
import crud.users
import config.db
from jwt_config import solicitar_token
from portadortoken import get_current_user, get_db
import schemas.users
import models.users
from typing import List

user = APIRouter()
security= HTTPBearer()

models.users.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@user.get("/users/",response_model=List[schemas.users.User], tags=["Usuarios"])
async def read_users(skip: int=0, limit: int=10, db: Session= Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_users = crud.users.get_users(db=db, skip=skip, limit=limit)
    return db_users

@user.post("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
async def read_user(id: int, db:Session=Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_user=crud.users.get_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/users/", response_model=schemas.users.User, tags=["Usuarios"])
def create_user(user: schemas.users.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_usuario(db, usuario = user.nombreUsuario)
    if db_user:
        raise HTTPException(status_code=400, detail="Usuario existente, intenta nuevamente")
    return crud.users.create_user(db=db, user=user)

@user.put("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
async def update_user(id: int, user: schemas.users.UserUpdate, db:Session=Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_user=crud.users.update_user(db=db, id=id, user=user)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.delete("/user/{id}", response_model=schemas.users.User, tags=["Usuarios"])
async def delete_user(id: int, db:Session=Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_user=crud.users.delete_user(db=db, id=id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@user.post("/login", tags=["Usuarios"])
def login(user: schemas.users.UserLogin, db: Session = Depends(get_db)):
    db_user = crud.users.get_user_by_email(db, email=user.correoElectronico)
    if not db_user or db_user.contrasena != user.contrasena:
        raise HTTPException(status_code=401, detail="Correo electrónico o contraseña incorrectos")
    
    access_token = create_access_token(data={"sub": user.correoElectronico})
    return {"message": "Acceso Correcto", "access_token": access_token}