from server import app

from flask import request
from flask import render_template


@app.route("/books", methods=["GET", "POST"])
def books():
    return render_template("books.html")
