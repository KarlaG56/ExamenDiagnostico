from src.Databases.MySQL.connection import Base
from sqlalchemy import Column, String, Integer


class Alumnos(Base):
    __tablename__ = 'alumnos'
    uuid = Column(String(36), primary_key=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    grado = Column(Integer, nullable=False)
    grupo = Column(String(1), nullable=False)

    def responsed(self):
        alumno_data = {
            "uuid": self.uuid,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "grado": self.grado,
            "grupo": self.grupo
        }
        return alumno_data
