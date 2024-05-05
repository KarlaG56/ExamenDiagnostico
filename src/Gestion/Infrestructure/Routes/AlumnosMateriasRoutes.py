from flask import Blueprint, request
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.AlumnosMateriasRepository import AlumnosMateriasRepository
from src.Gestion.Infrestructure.Controllers.AlumnosMaterias import Get, Create

repo = AlumnosMateriasRepository()
create_controller = Create.CreateController(repo)
get_controller = Get.GetController(repo)

alumnos_materias_routes = Blueprint('alumnos_materias_routes', __name__)

@alumnos_materias_routes.route('/<string:alumno_uuid>', methods=['GET'])
def get_alumnos_materias(alumno_uuid):
    return get_controller.run(alumno_uuid)

@alumnos_materias_routes.route('/', methods=['POST'])
def create_alumnos_materias():
    return create_controller.run(request)
