from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship, backref
from src.Databases.MySQL.connection import Base
from src.Gestion.Infrestructure.Models.MySQLModels.Tutores import Tutores
from src.Gestion.Infrestructure.Models.MySQLModels.Alumnos import Alumnos


class TutoresAlumnos(Base):
    __tablename__ = 'tutores_alumnos'
    uuid = Column(String(36), primary_key=True)
    alumno_uuid = Column(String(36), ForeignKey('alumnos.uuid'))
    alumno = relationship(Alumnos, backref=backref('tutores_alumnos', uselist=True, cascade="all, delete-orphan"))
    tutor_uuid = Column(String(36), ForeignKey('tutores.uuid'))
    tutor = relationship(Tutores, backref=backref('tutores_alumnos', uselist=True, cascade="all, delete-orphan"))

    def responsed(self):
        return {
            'uuid': self.uuid,
            'alumno': self.alumno.responsed(),
            'tutor': self.tutor.responsed()
        }
