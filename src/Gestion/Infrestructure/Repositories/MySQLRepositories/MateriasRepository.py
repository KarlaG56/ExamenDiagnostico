from src.Gestion.Domain.Entities.Materias import Materias
from src.Gestion.Domain.Ports.MateriasPort import MateriasPort
from src.Databases.MySQL.connection import Base, engine, session_local
from src.Gestion.Infrestructure.Models.MySQLModels.Materias import Materias as Model


class MateriasRepository(MateriasPort):
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session_local()

    def getMaterias(self):
        return [m.responsed() for m in self.session.query(Model).all()]

    def createMaterias(self, materias: Materias):
        new = Model(**materias.__dict__)
        self.session.add(new)
        self.session.commit()
        return new.responsed(), 201
