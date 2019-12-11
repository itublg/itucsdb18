from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
from hashlib import md5
import db

loginB = Blueprint('loginB', __name__,
                        template_folder='templates')

@loginB.route("/logged", methods = ['GET'])
def logged_func():
    with db.dataBaseLock:
        print(session.get('logged_in'))
        if not session.get('logged_in'):
            return redirect(url_for('loginB.login_func'))
        
        cursor = db.get_cursor()
        connection = db.get_connection()

        cursor.execute("""select friend from friends
                            where (username = %s) """, (session['username'],))

        friends = cursor.fetchall()

        cursor.execute("""select sender from friendrequests
                            where (friend = %s) """, (session['username'],))
        
        friendRequests = cursor.fetchall()

        print("rewuest", friendRequests)

        return redirect(url_for('profile.profileFuncMe'))

        #return render_template('logged.html', 
                  #      username = session['username'],
                   #     password = session['password'], 
                    #    friends = friends,
                     #   friendRequests = friendRequests)


@loginB.route("/login", methods = ['GET', 'POST'])
def login_func():
    with db.dataBaseLock:
        if session.get('logged_in'):
            return redirect(url_for('loginB.logged_func'))
        if request.method == 'POST':
            username = request.form.get('username')
            phash = md5(request.form.get('password').encode('utf-8')).hexdigest()
            cursor = db.get_cursor()
            cursor.execute("""select userpassword from users
                                where (username = %s or email = %s)""", (username, username))
            passTuple= cursor.fetchone()
            if passTuple == None:
                return render_template('login_form.html', error='Invalid username!')
                #return redirect(url_for('loginB.login_func')) #TODO username wrong
            passwdHash = passTuple[0]
            #print("paswd = ", passwdHash)
            #print("entered = ", phash)
            if passwdHash != phash:
                return render_template('login_form.html', error = 'Invalid password!')
                #return redirect(url_for('loginB.login_func')) #TODO password wrong
            
            session['username'] = request.form.get('username')
            session['password'] = phash
            session['logged_in'] = True
            return redirect(url_for('profile.profileFuncMe'))
            #return redirect(url_for('loginB.logged_func'))
        return render_template('login_form.html')


@loginB.route("/logout", methods = ['GET'])
def logout_func():
    session['logged_in'] = False
    return redirect(url_for('loginB.login_func'))
