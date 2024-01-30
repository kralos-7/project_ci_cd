from flask import render_template
from . import privado
import os
from helpers import *



@privado.route("/citas")
@login_required
def citas():
    return render_template("private/crud.html")

