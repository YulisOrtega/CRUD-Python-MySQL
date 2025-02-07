from sqlalchemy import Column,Integer, String,Enum
from config.db import Base
import enum

class TipoMaterial(str,enum.Enum):
    Computadora = "Computadora"
    Extensiones = "Extensiones"
    Cables = "Cables"
    Proyectores = "Proyectores"
    Conectores = "Conectores"
    
class Estatus(str,enum.Enum):
    Disponible ="Disponible"
    Prestado = "Prestado"
    Mantenimiento ="Matenimiento"
    Suspendido ="Suspendido"
    
class Material(Base): 
    __tablename__="tbb_materiales"
    
    id= Column(Integer, primary_key=True, autoincrement=True)
    tipoMaterial = Column(Enum(TipoMaterial))
    marca = Column(String(60))
    modelo = Column(String(100))    
    estatus = Column(Enum(Estatus))
