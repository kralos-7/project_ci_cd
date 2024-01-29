from flask import Blueprint
import os

# Se declara el blueprint para la vista pública
privado = Blueprint(
    "private",
    __name__,
    url_prefix="/",
    template_folder="templates",
)

# Se manda a llamar al archivo de los endpoints para la vista pública
from . import routes
