from . import autenticacion
from modules.auth.models.User import User, UserService
from database.db import db
from flask import request, jsonify, session, render_template, redirect
from datetime import datetime, timedelta
# from common import require_login, esta_logueado

NUM_MAX_INTENTOS = 3
DURACION_BLOQUEO = timedelta(minutes=1)

@autenticacion.route("/")
def index():
    return render_template("auth/index.html")


@autenticacion.route('/login',methods=['GET','POST'])
def login():
    mensaje = None
    now = datetime.utcnow()

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        # user = db.session.query(User).filter_by(email=email).first()
        user = UserService.authenticate_user(email)
        if user:
            if user.locked_until and now <= user.locked_until:
                
                mensaje = "Interfaz bloqueada. Inténtelo nuevamente después de 1 minuto."
            else:
                if user.login_attempts is None:
                    user.login_attempts = 0

                if user.check_password(password):
                    # Restablecer el contador de intentos si el inicio de sesión es exitoso
                    user.login_attempts = 0
                    db.session.commit()

                    session['email'] = user.email
                    session['username'] = user.get_username()
                    return redirect('/')
                else:
                    # Incrementar el contador de intentos
                    user.login_attempts += 1

                    if user.login_attempts >= NUM_MAX_INTENTOS:
                        # Bloquear la interfaz por 1 minuto
                        user.locked_until = now + DURACION_BLOQUEO
                        # Reiniciar los intentos después del bloqueo
                        user.login_attempts = 0

                    db.session.commit()
                    # print(f"Usuario después del commit: {user}")

                    if user.login_attempts >= NUM_MAX_INTENTOS:
                        mensaje = "Interfaz bloqueada."
                    else:
                        # intentos_disponibles = NUM_MAX_INTENTOS - user.login_attempts 
                        mensaje = "Usuario y/o contraseña incorrectos."
        else:
            mensaje = "El usuario no existe"

    return render_template('auth/index.html', mensajeIniciarSesion = mensaje)

@autenticacion.route('/register',methods=['GET','POST'])
def register():
    mensajeRegistrarse = None
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['passwordRegister']

        # validar = registrarse(username, email, password)
        new_user = db.session.query(User).filter_by(email=email).first()
        print(new_user)

        if new_user is None:
            UserService.create_user(username,email,password)
            return redirect('/')
        else:
            # El usuario ya existe, manejar según tus necesidades
            # return render_template("user_exists.html")
            print("entro al else")
            mensajeRegistrarse = "Usted no puede registrarse con este correo electrónico"

    # return render_template("register_form.html")
    return render_template("auth/index.html", mensajeRegistrarse = mensajeRegistrarse)



@autenticacion.route('/logout')
def logout():
    session.pop('email',None)
    session.pop('username', None)
    return redirect('/')