from flask import request
from flask import render_template
from server import app


@app.route("/books", methods=["GET", "POST"])
def books():
    return render_template()
