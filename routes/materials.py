from crud import materials
from fastapi import APIRouter, HTTPException, Depends
from models.materialss import Material
from sqlalchemy.orm import Session
import crud.materials
import config.db
import schemas.materials
import models.materialss
from typing import List

material = APIRouter()

models.materialss.Base.metadata.create_all(bind=config.db.engine)

def get_db():
    db = config.db.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@material.get("/materials/",response_model=List[schemas.materials.Material], tags=["Materiales"])
async def read_materials(skip: int=0, limit: int=10, db: Session= Depends(get_db)):
    db_materials = crud.materials.get_materials(db=db, skip=skip, limit=limit)
    return db_materials

@material.post("/material/{id}", response_model=schemas.materials.Material, tags=["Materiales"])
async def read_material(id: int, db:Session=Depends(get_db)):
    db_material=crud.materials.get_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.post("/materials/", response_model=schemas.materials.Material, tags=["Materiales"])
def create_material(material: schemas.materials.MaterialCreate, db: Session = Depends(get_db)):
    db_material = crud.materials.get_material_by_materials(db, material = material.tipoMaterial)
    if db_material:
        raise HTTPException(status_code=400, detail="Material existente, intenta nuevamente")
    return crud.materials.create_material(db=db, material=material)

@material.put("/material/{id}", response_model=schemas.materials.Material, tags=["Materiales"])
async def update_material(id: int, material: schemas.materials.MaterialUpdate, db:Session=Depends(get_db)):
    db_material=crud.materials.update_material(db=db, id=id, material=material)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material

@material.delete("/material/{id}", response_model=schemas.materials.Material, tags=["Materiales"])
async def delete_material(id: int, db:Session=Depends(get_db)):
    db_material=crud.materials.delete_material(db=db, id=id)
    if db_material is None:
        raise HTTPException(status_code=404, detail="Material not found")
    return db_material