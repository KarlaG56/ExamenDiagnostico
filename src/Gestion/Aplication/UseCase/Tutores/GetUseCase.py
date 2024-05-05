from src.Gestion.Domain.Ports.TutoresPort import TutoresPort as Port


class GetUseCase:
    def __init__(self, port: Port):
        self.repository = port

    def run(self):
        return self.repository.get_tutores()

