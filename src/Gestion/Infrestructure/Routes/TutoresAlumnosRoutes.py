from flask import Blueprint, request
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.TutoresAlumnosRepository import TutoresAlumnosRepository
from src.Gestion.Infrestructure.Controllers.TutoresAlumnos import Create, Get

repo = TutoresAlumnosRepository()
create_controller = Create.CreateController(repo)
get_controller = Get.GetController(repo)

tutores_alumnos_routes = Blueprint('tutores_alumnos_routes', __name__)

@tutores_alumnos_routes.route('/<string:tutor_uuid>', methods=['GET'])
def get_tutores_alumnos(tutor_uuid):
    return get_controller.run(tutor_uuid)

@tutores_alumnos_routes.route('/', methods=['POST'])
def create_tutores_alumnos():
    return create_controller.run(request)
