from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for


def login_required(f):
    """

    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session:
            return redirect(url_for('login', ))
        return f(*args, **kwargs)
    return decorated_function


def view(f):
    """
    to use this decorator properly, wait for arguements in target method.
    example in routes/home.py -> feed method
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, logged_in=True, username=session["logged_in"][4], **kwargs)
        else:
            return f(*args,**kwargs)
    return decorated_function

