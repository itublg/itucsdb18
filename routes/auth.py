from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint
from server import app

from routes.utils import *
from routes import home

from service.user import *


@app.route("/login", methods=["GET",  "POST"])
def login():
    if request.method == "GET":
        if "logged_in" in session:
            return home.feed()
        return render_template("login.html")
    user = get_user(request.form["email"], request.form["password"])
    if user is not None:
        session['logged_in'] = user
        return redirect("home")
    else:
        return render_template("login.html")


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    session.pop("logged_in", None)
    return home.home()


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if "logged_in" in session:
        return render_template("feed.html")

    if request.method == "GET":
        return render_template("signup.html")

    name = request.form["name"]
    surname = request.form["surname"]
    bday = request.form["bday"]
    email = request.form["email"]
    password = request.form["password"]
    username = request.form["username"]

    new_user = create_user(name, surname, username, password, email, bday)

    if new_user is None:
        return redirect("signup")

    return render_template("feed.html")
