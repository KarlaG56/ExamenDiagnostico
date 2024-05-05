from flask import Flask
from flask_cors import CORS

from src.Gestion.Infrestructure.Routes import AlumnosRoutes, TutoresRoutes, MateriasRoutes

app = Flask(__name__)

app.register_blueprint(AlumnosRoutes.alumnos_routes, url_prefix='/alumnos')
app.register_blueprint(TutoresRoutes.tutores_routes, url_prefix='/tutores')
app.register_blueprint(MateriasRoutes.materias_routes, url_prefix='/materias')
CORS(app)

if __name__ == '__main__':
    app.run(debug=True)
