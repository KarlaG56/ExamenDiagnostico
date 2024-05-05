from flask import Blueprint, request
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.MateriasRepository import MateriasRepository
from src.Gestion.Infrestructure.Controllers.Materias import Get, Create

repo = MateriasRepository()
create_controller = Create.CreateController(repo)
get_controller = Get.GetController(repo)

materias_routes = Blueprint('materias_routes', __name__)

@materias_routes.route('/', methods=['GET'])
def get_materias():
    return get_controller.run()

@materias_routes.route('/', methods=['POST'])
def create_materias():
    return create_controller.run(request)
