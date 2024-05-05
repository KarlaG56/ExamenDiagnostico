from src.Gestion.Infrestructure.Models.MySQLModels.TutoresAlumnos import TutoresAlumnos as Model
from src.Gestion.Domain.Entities.TutoresAlumnos import TuroresAlumnos
from src.Gestion.Domain.Ports.TutoresAlumnosPort import TutoresAlumnosPort
from src.Databases.MySQL.connection import Base, engine, session_local


class TutoresAlumnosRepository(TutoresAlumnosPort):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session_local()

    def getTuroresAlumnos(self):
        return [p.responsed() for p in self.session.query(TuroresAlumnos).all()]

    def crearTuroresAlumnos(self, turoresAlumnos: TuroresAlumnos):
        new = Model(**turoresAlumnos)
        self.session.add(new)
        self.session.commit()
        return new.responsed()