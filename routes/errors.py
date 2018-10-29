from flask import Flask, flash, redirect, render_template, request, session, abort, url_for
from server import app

from routes.utils import login_required,view

@app.errorhandler(404)
@view
def page_not_found(*arg,**kwargs):
    return render_template("404.html", **kwargs)