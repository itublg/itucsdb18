from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
import db

map_page = Blueprint('map_page', __name__,
                        template_folder='templates')

@map_page.route("/map", methods = ['GET'])
def map_func():
    city = ('Istanbul', 2)
    cities = [ [ ('empty', -1) for i in range(0, 12) ] for j in range(0, 12) ]
    cities[1][1] = city
    cities[4][5] = ('Adana', 1)
    return render_template('map_page.html', cities=cities)