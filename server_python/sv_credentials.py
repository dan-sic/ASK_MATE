from server_python.config import app
from flask import flash, render_template, redirect
from Forms import forms


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = forms.RegistrationForm()
    if form.validate_on_submit():
        print('works')
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect('/')
    return render_template('register.html', form=form, title='Register')
