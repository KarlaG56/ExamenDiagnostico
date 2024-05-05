from src.Databases.MySQL.connection import Base, engine, session_local
from src.Gestion.Infrestructure.Models.MySQLModels.AlumnosMaterias import AlumnosMaterias as Model
from src.Gestion.Domain.Entities.AlumnosMaterias import AlumnosMaterias
from src.Gestion.Domain.Ports.AlumnosMateriasPort import AlumnosMateriasPort


class AlumnosMateriasRepository(AlumnosMateriasPort):
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session_local()

    def getAlumnosMaterias(self, alumno_uuid):
        return [p.responsed() for p in self.session.query(Model).filter(Model.alumno_uuid == alumno_uuid).all()]

    def createAlumnosMaterias(self, alumnosMaterias: AlumnosMaterias):
        new = Model(**alumnosMaterias.__dict__)
        self.session.add(new)
        self.session.commit()
        return new.responsed(), 201
