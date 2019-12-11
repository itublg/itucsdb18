from flask import render_template, Blueprint, session, redirect, url_for

home = Blueprint('home', __name__,
                        template_folder='templates')
@home.route("/")
def home_page():
    if not session.get('logged_in'):
        return redirect(url_for('loginB.login_func'))
    
    return render_template('base.html')