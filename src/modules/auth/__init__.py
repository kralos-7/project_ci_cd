from flask import Blueprint, send_from_directory
import os

# Se declara el blueprint para la vista pública
# template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), "templates"))

autenticacion = Blueprint(
    "authentication",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
)


# Se manda a llamar al archivo de los endpoints para la vista pública
from . import routes
