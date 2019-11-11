from flask import Flask, render_template, request, redirect, url_for, session
from tables import tables
from home import home
from login import loginB
from signup import signup
from friends import friends
from my_cities import my_cities
from our_team import our_team
import os
import sys
import threading
import psycopg2 as dbapi2
import atexit
import db

import update

from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)
app.register_blueprint(tables)
app.register_blueprint(home)
app.register_blueprint(loginB)
app.register_blueprint(signup)
app.register_blueprint(friends)
app.register_blueprint(my_cities)
app.register_blueprint(our_team)
app.secret_key = b'_383#y2L"F4Q8z]/'
# cok gizli


def test_job():
    with db.dataBaseLock:
        cursor = db.get_cursor()
        connection = db.get_connection()
        cursor.execute("""INSERT INTO DUMMY VALUES (%s)""", ('10',))
        connection.commit()

scheduler = BackgroundScheduler()
job = scheduler.add_job(test_job, 'interval', seconds=5)
scheduler.start()


# @app.route("/")
# def home_page():
#     connection, cursor = testFonk()
#     cursor.execute("select * from dummy")
#     a = cursor.fetchall()    
#     returnStr = "deneme<br>"
#     for x in a:
#         for i in x:
#             returnStr += str(i)
#         returnStr +="<br>"
#     connection.close()
#     cursor.close()
#     return returnStr
#     #return render_template('base.html')



if __name__ == "__main__":

    update.gameThread = threading.Timer(update.POOL_TIME, update.update, ())
    update.gameThread.start()

    
    app.run(host='0.0.0.0', port=5000)
