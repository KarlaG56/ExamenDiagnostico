from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Databases.MySQL.connection import Base
from src.Gestion.Infrestructure.Models.MySQLModels.Materias import Materias
from src.Gestion.Infrestructure.Models.MySQLModels.Alumnos import Alumnos

class AlumnosMaterias(Base):
    __tablename__ = 'alumnos_materias'
    uuid = Column(String(36), primary_key=True)
    alumno_uuid = Column(String(36), ForeignKey('alumnos.uuid'), nullable=False)
    alumno = relationship(Alumnos, backref=backref('alumnos_materias', uselist=True, cascade="all, delete-orphan"))
    materia_uuid = Column(String(36), ForeignKey('materias.uuid'), nullable=False)
    materia = relationship(Materias, backref=backref('alumnos_materias', uselist=True, cascade="all, delete-orphan"))

    def responsed(self):
        return {
            'uuid': self.uuid,
            'alumno': self.alumno.responsed(),
            'materia': self.materia.responsed()
        }