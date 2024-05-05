from src.Gestion.Infrestructure.Models.MySQLModels.Alumnos import Alumnos as Model
from src.Gestion.Domain.Entities.Alumnos import Alumnos
from src.Gestion.Domain.Ports.AlumnosPort import AlumnosPort
from src.Databases.MySQL.connection import Base, engine, session_local


class AlumnosRepository(AlumnosPort):
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session_local()

    def getAlumnos(self):
        return [a.responsed() for a in self.session.query(Model).all()]

    def createAlumnos(self, alumno: Alumnos):
        new = Model(**alumno.__dict__)
        self.session.add(new)
        self.session.commit()
        return new.responsed(), 201


