from src.Databases.MySQL.connection import Base
from sqlalchemy import Column, String, Integer

class Tutores(Base):
    __tablename__ = 'tutores'
    uuid = Column(String(36), primary_key=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    horas = Column(Integer, nullable=False)
    titulo = Column(String(255), nullable=False)

    def responsed(self):
        tutor_data = {
            "uuid": self.uuid,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "horas": self.horas,
            "titulo": self.titulo
        }
        return tutor_data