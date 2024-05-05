from abc import ABC, abstractmethod
from src.Gestion.Domain.Entities.Materias import Materias


class MateriasPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def getMaterias(self):
        pass

    @abstractmethod
    def createMaterias(self, materias: Materias):
        pass
