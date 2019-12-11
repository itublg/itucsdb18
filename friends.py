from flask import Flask, render_template, request, redirect, url_for, session, Blueprint, flash
from hashlib import md5
import db
from statements import friend_request, insert_friend, delete_friend, accept_friend, reject_friend
friends = Blueprint('friends', __name__,
                        template_folder='templates')


@friends.route("/friendAdd", methods = ['POST'])
def add():
    if not session.get('logged_in'):
        return redirect(url_for('loginB.login_func'))
    with db.dataBaseLock:
        cursor = db.get_cursor()
        connection = db.get_connection()
        username = request.form.get('username')
        if username == session['username']:
            return render_template('logged.html', error='it is you')
        #print("username", username)
        if len(username) < 5:
            return render_template('logged.html', error='username is too short (min 5 char)')

        cursor.execute("""select userpassword from users
                            where (username = %s) """, (username,))

        passTuple= cursor.fetchone()
        if passTuple == None:
            return render_template('logged.html', error='user not found')
        cursor.execute("""select username,friend from friends where(username=%s and friend=%s)""",
                        (session['username'], username))
        is_friend = cursor.fetchone()
        if is_friend is not None:
            return render_template('logged.html', error='Already friend')
        try:
            friend_request(cursor, session['username'], username)
        except:
            return render_template('logged.html', error='error')
        finally:
            connection.commit()
            return redirect(url_for('leaderboard.leaderboardFunction'))
            #return render_template('logged.html', error='friend request sent')

@friends.route("/friendDelete", methods = ['POST'])
def deleteFriend():
    if not session.get('logged_in'):
        return redirect(url_for('loginB.login_func'))
    with db.dataBaseLock:
        cursor = db.get_cursor()
        connection = db.get_connection()
        username = request.form.get('username')

        is_friend = delete_friend(cursor, session['username'], username) # if successfully deletes return 1
                                                                         # else return 0
        connection.commit()

        if not is_friend:
            return render_template('logged.html', error='User not friend')

        return redirect(session['url'])

@friends.route("/friendAccept", methods = ['POST'])
def accept():
    with db.dataBaseLock:
        cursor = db.get_cursor()
        connection = db.get_connection()
        username = request.form.get('username')
        #print("accept ", username)
        # is it worth to befriend a person like him/her
        is_acceptable = accept_friend(cursor, session['username'], username)

        if is_acceptable == 0:
            return render_template('logged.html', error="error") #no such request
        elif is_acceptable == 1:
            if username:
                insert_friend(cursor, session['username'], username)
        connection.commit()
        if session['url']:
            return redirect(session['url'])
        else:
            return redirect(url_for('profile.profileFuncMe'))

@friends.route("/friendReject", methods = ['POST'])
def reject():
    with db.dataBaseLock:
        cursor = db.get_cursor()
        connection = db.get_connection()
        username = request.form.get('username')
        #print("accept ", username)
        # is it worth to befriend a person like him/her
        reject_friend(cursor, session['username'], username)
        connection.commit()
        if session['url']:
            return redirect(session['url'])
        else:
            return redirect(url_for('profile.profileFuncMe'))
