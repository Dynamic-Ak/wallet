from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SignupForm(FlaskForm):
    username = StringField(
        'Username',
        validators=[
            DataRequired(),
            Length(min=3, max=10, message='Must be 3 to 10 characters long')
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            EqualTo('confirm', message='Passwords do not match'),
            Length(min=4, max=10, message='Must be 4 to 10 characters long')
        ]
    )
    confirm = PasswordField(
        'Repeat Password',
        validators=[DataRequired()]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email()
        ]
    )
    submit = SubmitField('Sign Up')
