from src.Gestion.Infrestructure.Models.MySQLModels.Tutores import Tutores as Model
from src.Gestion.Domain.Entities.Turores import Tutores
from src.Gestion.Domain.Ports.TutoresPort import TutoresPort
from src.Databases.MySQL.connection import Base, engine, session_local


class TutoresRepository(TutoresPort):
    def __init__(self):
        Base.metadata.create_all(engine)
        self.session = session_local()

    def get_tutores(self):
        return [t.responsed() for t in self.session.query(Model).all()]

    def create_tutores(self, tutor: Tutores):
        new = Model(**tutor.__dict__)
        self.session.add(new)
        self.session.commit()
        return new.responsed(), 201

