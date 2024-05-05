from src.Databases.MySQL.connection import Base, engine, session_local
from src.Gestion.Infrestructure.Models.MySQLModels.AlumnosMaterias import AlumnosMaterias as Model
from src.Gestion.Domain.Entities.AlumnosMaterias import AlumnosMaterias
from src.Gestion.Domain.Ports.AlumnosMateriasPort import AlumnosMateriasPort


class AlumnosMateriasRepository(AlumnosMateriasPort):
    def __init__(self):
        pass

    def getAlumnosMaterias(self):
        pass

    def createAlumnosMaterias(self, alumnosMaterias: AlumnosMaterias):
        pass