from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from data_manager import dm_users

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=30)])
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=60)])
    confirmed_password = PasswordField('Confirm password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        is_user = bool(dm_users.get_user(username=username.data))
        if is_user:
            raise ValidationError('This username is taken. Please choose another one!')

    def validate_email(self, email):
        is_user = bool(dm_users.get_user(email=email.data))
        if is_user:
            raise ValidationError('This email is taken. Please choose another one!')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')