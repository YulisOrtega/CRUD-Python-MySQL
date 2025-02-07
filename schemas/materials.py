from typing import List, Union, Optional
from pydantic import BaseModel
from datetime import datetime

class MaterialBase(BaseModel):
    tipoMaterial: str
    marca: str
    modelo: str
    estatus:str
    
class MaterialCreate(MaterialBase):
    pass
class MaterialUpdate(MaterialBase):
    pass
class Material(MaterialBase):
    id:int
    class Config:
        orm_mode=True
        