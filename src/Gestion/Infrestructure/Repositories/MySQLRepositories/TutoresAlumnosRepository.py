from src.Gestion.Infrestructure.Models.MySQLModels.TutoresAlumnos import TutoresAlumnos as Model
from src.Gestion.Domain.Entities.TutoresAlumnos import TuroresAlumnos
from src.Gestion.Domain.Ports.TutoresAlumnosPort import TutoresAlumnosPort
from src.Databases.MySQL.connection import Base, engine, session_local


class TutoresAlumnosRepository(TutoresAlumnosPort):

    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session_local()

    def getTuroresAlumnos(self, tutor_uuid):
        return [p.responsed() for p in self.session.query(Model).filter(Model.tutor_uuid == tutor_uuid).all()]

    def crearTuroresAlumnos(self, turoresAlumnos: TuroresAlumnos):
        new = Model(**turoresAlumnos.__dict__)
        self.session.add(new)
        self.session.commit()
        return new.responsed(), 201
