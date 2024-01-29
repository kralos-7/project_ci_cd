from . import autenticacion
from flask import request, jsonify, session, render_template, redirect
# from common import require_login, esta_logueado

@autenticacion.route("/")
def index():
    return render_template("auth/index.html")



@autenticacion.route("/login", methods=["POST"])
def login():
    #validaciones a la bd
    data = request.get_json()
    user = data.get('campoUsuario')
    password = data.get('campoPassword')
    if password == "123":
        session['email'] = "correo@dominio.com"
        session['username'] = "Luiz Ruiz"
        # session["login"] = "usuario1"
        return jsonify({"ok":True,"mensaje": "Usuario y/o contraseña válidos. Por favor vuelva a intentarlo"}),200

    else:
        return jsonify({"ok":False,"mensaje": "Usuario y/o contraseña inválidos. Por favor vuelva a intentarlo"}),401



@autenticacion.route("/sign-up")
def sign_up():
    return "sign-up"

@autenticacion.route('/logout')
def logout():
    session.pop('email',None)
    session.pop('username', None)
    return redirect('/')