from flask import Flask, flash, redirect, render_template, request, session, abort
from flask import Blueprint
from server import app

from routes.utils import login_required,view

@app.route("/", methods=["GET", "POST"])
@app.route("/index", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@view
def home(*args, **kwargs):
    if session.get("logged_in") is not None:
        return render_template("feed.html", **kwargs)
    else:
        return render_template("index.html", **kwargs)

@app.route("/feed", methods=["GET"])
@login_required
@view
def feed(*args, **kwargs):
    print(kwargs)
    return render_template("feed.html", posts = range(200), **kwargs )