from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from server import app

from endpoints.utils import login_required, view


@app.errorhandler(404)
@view
def pageNotFoundEnd(*arg, **kwargs):
    print("error 404")
    return render_template("errors/404.html", **kwargs)

@app.errorhandler(403)
@app.route("/unathorized-operation", methods=["GET"])
@view
def unathorized(*arg, **kwargs):
    return render_template("errors/403.html", **kwargs)



