from src.Gestion.Domain.Ports.TutoresAlumnosPort import TutoresAlumnosPort as Port


class GetUseCase:
    def __init__(self, port: Port):
        self.repository = port

    def run(self, tutor_uuid):
        return self.repository.getTuroresAlumnos(tutor_uuid)
