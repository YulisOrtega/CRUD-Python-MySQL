import datetime
import models.prestamoss
import schemas.prestamos
from sqlalchemy.orm import Session

def get_prestamo(db:Session, id: int):
    return db.query(models.prestamoss.Prestamo).filter(models.prestamoss.Prestamo.id==id).first()

def get_prestamo_by_prestamos(db:Session, prestamo: str):
    return db.query(models.prestamoss.Prestamo).filter(models.prestamoss.Prestamo.fechaPrestamo == prestamo).first()

def get_prestamos(db:Session, skip: int =0, limit: int=0):
    return db.query(models.prestamoss.Prestamo).offset(skip).limit(limit).all()


def create_prestamo(db: Session, prestamo: schemas.prestamos.PrestamoCreate):
    db_prestamo = models.prestamoss.Prestamo(
        id_usuario = prestamo.id_usuario,
        id_material = prestamo.id_material,
        fechaPrestamo = prestamo.fechaPrestamo,
        fechaDevolucion = prestamo.fechaDevolucion,
        estatusPrestamo = prestamo.estatusPrestamo,
        )
    db.add(db_prestamo)
    db.commit()
    db.refresh(db_prestamo)
    return db_prestamo

def update_prestamo(db:Session, id:int, prestamo:schemas.prestamos.PrestamoUpdate):
    db_prestamo = db.query(models.prestamoss.Prestamo).filter(models.prestamoss.Prestamo.id == id).first()
    if db_prestamo:
        for var, value in vars(prestamo).items():
            setattr(db_prestamo, var, value) if value else None
        db.commit()
        db.refresh(db_prestamo)
    return db_prestamo

def delete_prestamo(db:Session, id:int):
    db_prestamo = db.query(models.prestamoss.Prestamo).filter(models.prestamoss.Prestamo.id == id).first()
    if db_prestamo:
        db.delete(db_prestamo)
        db.commit()
    return db_prestamo