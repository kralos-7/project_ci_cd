from flask import Blueprint

# Se declara el blueprint para la vista pública
publico = Blueprint(
    "public",
    __name__,
    url_prefix="/",
    template_folder="templates",
    static_folder="static",
)

# Se manda a llamar al archivo de los endpoints para la vista pública
from . import routes
# import routes
