from sqlalchemy import Column,Integer, String, DateTime,Enum
from config.db import Base
import enum
    
class Estatus(str,enum.Enum):
    Activo ="Activo"
    Devuelto = "Devuelto"
    Vencido ="Vencido"
    
class Prestamo(Base): 
    __tablename__="tbb_prestamos"
    
    id= Column(Integer, primary_key=True, autoincrement=True)
    id_usuario= Column(Integer)
    id_material= Column(Integer)
    fechaPrestamo = Column(DateTime)
    fechaDevolucion = Column(String(60))
    estatusPrestamo = Column(Enum(Estatus))