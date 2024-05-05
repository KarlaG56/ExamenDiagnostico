from src.Databases.MySQL.connection import Base
from sqlalchemy import Column, String


class Materias(Base):
    __tablename__ = 'materias'
    uuid = Column(String(36), primary_key=True)
    nombre = Column(String(255), nullable=False)

    def responsed(self):
        materia_data = {
            'uuid': self.uuid,
            'nombre': self.nombre
        }
        return materia_data
