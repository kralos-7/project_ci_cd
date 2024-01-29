from flask import render_template
from . import publico


@publico.route("/")
def index():
    return render_template("public/index.html")

