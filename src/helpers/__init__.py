from flask import redirect, session, url_for
from functools import wraps

def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'email' not in session:
            return redirect(url_for('public.index'))
        return f(*args, **kwargs)
    return decorated_function

def esta_logueado():
    return 'email' in session