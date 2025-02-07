import models.materialss
import schemas.materials
from sqlalchemy.orm import Session

def get_material(db:Session, id: int):
    return db.query(models.materialss.Material).filter(models.materialss.Material.id==id).first()

def get_material_by_materials(db:Session, material: str):
    return db.query(models.materialss.Material).filter(models.materialss.Material.tipoMaterial == material).first()

def get_materials(db:Session, skip: int =0, limit: int=0):
    return db.query(models.materialss.Material).offset(skip).limit(limit).all()

def create_material(db: Session, material: schemas.materials.MaterialCreate):
    db_material = models.materialss.Material(
        tipoMaterial = material.tipoMaterial,
        marca = material.marca,
        modelo = material.modelo,
        estatus = material.estatus,
        )
    db.add(db_material)
    db.commit()
    db.refresh(db_material)
    return db_material

def update_material(db:Session, id:int, material:schemas.materials.MaterialUpdate):
    db_material = db.query(models.materialss.Material).filter(models.materialss.Material.id == id).first()
    if db_material:
        for var, value in vars(material).items():
            setattr(db_material, var, value) if value else None
        db.commit()
        db.refresh(db_material)
    return db_material

def delete_material(db:Session, id:int):
    db_material = db.query(models.materialss.Material).filter(models.materialss.Material.id == id).first()
    if db_material:
        db.delete(db_material)
        db.commit()
    return db_material