from src.Gestion.Domain.Entities.Turores import Tutores
from abc import ABC, abstractmethod


class TutoresPort(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_tutores(self):
        pass

    @abstractmethod
    def create_tutores(self, tutor: Tutores):
        pass
