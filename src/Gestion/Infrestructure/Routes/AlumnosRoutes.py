from flask import Blueprint, request
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.AlumnosRepository import AlumnosRepository
from src.Gestion.Infrestructure.Controllers.Alumnos import Get, Create

repo = AlumnosRepository()
create_crontroller = Create.CreateController(repo)
get_controller = Get.GetController(repo)

alumnos_routes = Blueprint('alumnos_routes', __name__)

@alumnos_routes.route('/', methods=['GET'])
def get_alumnos():
    return get_controller.run()

@alumnos_routes.route('/', methods=['POST'])
def create_alumnos():
    return create_crontroller.run(request)
