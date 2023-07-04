from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError
from mercado.models import User

class CadastroForm(FlaskForm):
    def validate_user(self, user):
        user = User.query.filter_by(user=user.data).first()
        if user:
            raise ValidationError('Username already exists! Please try a different username.')
    
    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email:
            raise ValidationError('Email already exists! Please try a different email.')
    
    def validate_password1(self, password1):
        if len(password1.data) < 6:
            raise ValidationError('Password must be at least 6 characters long.')
        
    user = StringField(label="Username: ", validators=[Length(min=2, max=30), DataRequired()])
    email = StringField(label='Email: ', validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password: ', validators=[Length(min=6), DataRequired()])
    password2 = PasswordField(label='Confirm Password: ', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Register')

class LoginForm(FlaskForm):
    user = StringField(label="Username: ", validators=[DataRequired()])
    password = PasswordField(label='Password: ', validators=[DataRequired()])
    submit = SubmitField(label='Login')
