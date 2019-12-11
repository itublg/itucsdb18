from flask import render_template, Blueprint, session, redirect, url_for
import db
my_cities = Blueprint('city', __name__,
                        template_folder='templates')



@my_cities.route("/my_cities")
def cities_page():
    # username = session['username']
    # cursor = db.get_cursor()
    # cursor.execute("""
    # SELECT * FROM CITY WHERE (CITY_MAJOR = %s)
    # """, (username,))
    # cities = cursor.fetchall()

    cities = []
    return render_template("cities.html", cities=cities)
