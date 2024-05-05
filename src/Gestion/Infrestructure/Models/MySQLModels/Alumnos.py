from src.Databases.MySQL.connection import Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Gestion.Infrestructure.Models.MySQLModels.Tutores import Tutores


class Alumnos(Base):
    __tablename__ = 'alumnos'
    uuid = Column(String(36), primary_key=True)
    nombre = Column(String(255), nullable=False)
    apellido = Column(String(255), nullable=False)
    grado = Column(Integer, nullable=False)
    grupo = Column(String(1), nullable=False)
    tutor_uuid = Column(String(36), ForeignKey('tutores.uuid'), nullable=True)
    tutor = relationship(Tutores, backref=backref('tutores_alumnos', uselist=True, cascade="all, delete-orphan"))

    def responsed(self):
        alumno_data = {
            "uuid": self.uuid,
            "nombre": self.nombre,
            "apellido": self.apellido,
            "grado": self.grado,
            "grupo": self.grupo
        }
        return alumno_data
