from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class CadastroForm(FlaskForm):
    user = StringField(label="Username: ")
    email = StringField(label='Email: ')
    password1 = PasswordField(label='Password: ')
    password2 = PasswordField(label='Confirm Password: ')
    submit = SubmitField(label='Register')
