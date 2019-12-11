from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
from hashlib import md5
import db
from statements import insert_user
signup = Blueprint('signup', __name__,
                        template_folder='templates')


@signup.route("/signup", methods = ['GET', 'POST'])
def signup_func():
    with db.dataBaseLock:
        if session.get('logged_in'):
            return redirect(url_for('loginB.logged_func'))
        if request.method == 'POST':

            cursor = db.get_cursor()
            connection = db.get_connection()

            username = request.form.get('username')
            print("username", username)
            email = request.form.get('email')
            password = request.form.get('password')
            if len(password) < 8:
                return render_template('signup_form.html', error='password is too short (min. 8 char)')
            if len(username) < 5:
                return render_template('signup_form.html', error='username is too short (min 5 char)')


            cursor.execute("""select userpassword from users
                                where (username = %s) """, (username,))

            passTuple= cursor.fetchone()
            if passTuple != None:
                return render_template('signup_form.html', error='username is already taken')


            cursor.execute("""select userpassword from users
                                where (email = %s )""", (email,))

            passTuple= cursor.fetchone()
            if passTuple != None:
                return render_template('signup_form.html', error='email is already used')


            phash = md5(request.form.get('password').encode('utf-8')).hexdigest()
            insert_user(cursor,username, phash, email)
            connection.commit()
            session['username'] = username
            session['password'] = phash
            session['logged_in'] = True
            return redirect(url_for('loginB.logged_func'))
        return render_template('signup_form.html')
