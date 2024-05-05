from src.Gestion.Domain.Ports.AlumnosPort import AlumnosPort


class GetUseCase:
    def __init__(self, port: AlumnosPort):
        self.repository = port

    def run(self):
        return self.repository.getAlumnos()
