from flask import Flask, render_template, Blueprint, session, redirect, url_for
import os
import sys

import psycopg2 as dbapi2

import db

tables = Blueprint('tables', __name__,
                        template_folder='templates')

@tables.route("/tables")
def home_page():
    with db.dataBaseLock:
        if not session.get('logged_in'):
            return redirect(url_for('loginB.login_func'))
        else:
            print (session.get('username'))
        # connection, cursor = testFonk()
        cursor = db.get_cursor()
        cursor.execute("select * from dummy")
        a = cursor.fetchall()    
        returnStr = "deneme<br>"
        for x in a:
            for i in x:
                returnStr += str(i)
            returnStr +="<br>"

        return returnStr
