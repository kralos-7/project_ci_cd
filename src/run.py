from Server import Backend
from modules.auth import autenticacion
from modules.public import publico  
from modules.private import privado 
from config import DevelopmentConfig

app = Backend(__name__, DevelopmentConfig, autenticacion, publico, privado)

if __name__ == "__main__":
    app.run()
