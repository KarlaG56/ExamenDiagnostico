from flask import Blueprint, request
from src.Gestion.Infrestructure.Repositories.MySQLRepositories.TutoresRepository import TutoresRepository
from src.Gestion.Infrestructure.Controllers.Tutores import Get, Create


repo = TutoresRepository()
create_controller = Create.CreateController(repo)
get_controller = Get.GetController(repo)

tutores_routes = Blueprint('tutores_routes', __name__)

@tutores_routes.route('/', methods=['GET'])
def get_tutores():
    return get_controller.run()

@tutores_routes.route('/', methods=['POST'])
def create_tutores():
    return create_controller.run(request)
