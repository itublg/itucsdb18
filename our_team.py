from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash

our_team = Blueprint('our_team', __name__,
                        template_folder='templates')

@our_team.route("/our_team", methods = ['GET'])
def ourteam():
    return render_template('our_team.html')
