from flask import request
from flask import render_template
from flask import Blueprint
from server import app

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return render_template("index.html")

