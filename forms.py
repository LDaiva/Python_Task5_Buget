from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FloatField, EmailField
from wtforms.validators import Email, DataRequired, EqualTo, ValidationError, InputRequired
import app


class RegisterForm(FlaskForm):
    name = StringField('Name', [DataRequired()])
    email = EmailField('Email', [InputRequired()])
    password = PasswordField('Password', [DataRequired()])
    confirm_password = PasswordField(
        'Repeat password', [DataRequired(), EqualTo('password', 'Passwords must match')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        with app.app.app_context():
            user = app.User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('This email is already in use')

    def validate_name(self, name):
        with app.app.app_context():
            user = app.User.query.filter_by(name=name.data).first()
            if user:
                raise ValidationError('This name is already in use')


class LoginForm(FlaskForm):
    email = EmailField('Email', [InputRequired()])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')


class EntryForm(FlaskForm):
    income = BooleanField('Income')
    sum = FloatField('Sum', [DataRequired()])
    submit = SubmitField('Submit')


class ProfForm(FlaskForm):
    name = StringField('Vardas', [DataRequired()])
    email = EmailField('El.pastas', [InputRequired()])
    submit = SubmitField('Atnaujinti')
