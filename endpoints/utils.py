from functools import wraps
from flask import Flask, flash, redirect, render_template, request, session, abort, url_for


def login_required(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" not in session:
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


def view(f):

    @wraps(f)
    def decorated_function(*args, **kwargs):
        if "logged_in" in session:
            return f(*args, logged_in=True, username=session["logged_in"][1], userid=session["logged_in"][0],  **kwargs)
        else:
            return f(*args, **kwargs)
    return decorated_function
def login_required_action(f):

    def decorated_function(*args, **kwargs):
        if "logged_in" not in session:
            return redirect('unauthorized-operation')
        return f(*args, **kwargs)
    return decorated_function
