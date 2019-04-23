from server_python.config import app
from data_manager import dm_general
from flask import Flask, session, redirect, url_for, escape, request

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # remove the username from the session if it's there
    if request.method == 'POST':
        session.pop('username', None)
        return redirect(url_for('index'))
