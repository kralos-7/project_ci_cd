from flask import render_template
from . import privado
import os


@privado.route("/citas")
def citas():
    return render_template("private/crud.html")

