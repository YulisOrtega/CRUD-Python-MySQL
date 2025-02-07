from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class PrestamoBase(BaseModel):
    id_usuario: int
    id_material: int
    fechaPrestamo: datetime
    fechaDevolucion: str
    estatusPrestamo:str
    
class PrestamoCreate(PrestamoBase):
    pass
class PrestamoUpdate(PrestamoBase):
    pass
class Prestamo(PrestamoBase):
    id:int
    class Config:
        orm_mode=True
        