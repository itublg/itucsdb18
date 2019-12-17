from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from flask import Blueprint
from server import app

from endpoints.utils import login_required, view
from model.dummies import *


@app.route("/init", methods=["GET"])
def init():

    DeleteAllTable()
    CreateAllTable()
    CreateStarter()


    return redirect(url_for('home'))


@app.route("/", methods=["GET"])
@app.route("/index", methods=["GET"])
@app.route("/home", methods=["GET"])
@view
def home(*args, **kwargs):

    if session.get("logged_in") is not None:
        print("logged")
        return redirect(url_for("user.feed"))
    else:
        print("hi I am here")
        return render_template("index.html", **kwargs)



@app.route("/about", methods=["GET"])
@view
def about(*args, **kwargs):
    if session.get("logged_in") is not None:
        print("logged")
        return render_template("loginAbout.html")

    else:
        return render_template("about.html")
