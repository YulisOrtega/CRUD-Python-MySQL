from fastapi import APIRouter, HTTPException, Depends
from portadortoken import get_current_user, get_db
from sqlalchemy.orm import Session
import crud.prestamos
import config.db
import schemas.prestamos
import models.prestamoss
from typing import List

prestamo = APIRouter()

models.prestamoss.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@prestamo.get("/prestamos/",response_model=List[schemas.prestamos.Prestamo], tags=["Prestamos"])
async def read_prestamos(skip: int=0, limit: int=10, db: Session= Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_prestamos = crud.prestamos.get_prestamos(db=db, skip=skip, limit=limit)
    return db_prestamos

@prestamo.post("/prestamo/{id}", response_model=schemas.prestamos.Prestamo, tags=["Prestamos"])
async def read_prestamo(id: int, db:Session=Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_prestamo=crud.prestamos.get_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo

@prestamo.post("/prestamos/", response_model=schemas.prestamos.Prestamo, tags=["Prestamos"])
def create_user(prestamo: schemas.prestamos.PrestamoCreate, db: Session = Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_prestamo = crud.prestamos.get_prestamo_by_prestamos(db, prestamo = prestamo.fechaPrestamo)
    if db_prestamo:
        raise HTTPException(status_code=400, detail="Prestamo existente, intenta nuevamente")
    return crud.prestamos.create_prestamo(db=db, prestamo=prestamo)

@prestamo.put("/prestamo/{id}", response_model=schemas.prestamos.Prestamo, tags=["Prestamos"])
async def update_prestamo(id: int, prestamo: schemas.prestamos.PrestamoUpdate, db:Session=Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_prestamo=crud.prestamos.update_prestamo(db=db, id=id, prestamo=prestamo)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo

@prestamo.delete("/prestamo/{id}", response_model=schemas.prestamos.Prestamo, tags=["Prestamos"])
async def delete_prestamo(id: int, db:Session=Depends(get_db), current_user: schemas.users.User = Depends(get_current_user)):
    db_prestamo=crud.prestamos.delete_prestamo(db=db, id=id)
    if db_prestamo is None:
        raise HTTPException(status_code=404, detail="Prestamo no encontrado")
    return db_prestamo