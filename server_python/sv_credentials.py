from server_python.config import app
from flask import flash, render_template, session, redirect, url_for, escape, request
from Forms import forms


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        print('works')
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect('/')
    return render_template('register.html', form=form, title='Register')


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

