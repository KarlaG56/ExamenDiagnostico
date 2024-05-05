from src.Gestion.Domain.Ports.MateriasPort import MateriasPort as Port


class GetUseCase:
    def __init__(self, port: Port):
        self.repository = port

    def run(self):
        return self.repository.getMaterias()
