
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, validators, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length

class loginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

class testPostForm(FlaskForm):
    nome = StringField('nome', [validators.Length(min=2, max=25)])
    cognome = StringField('cognome', [validators.Length(min=2, max=35)])
    submit = SubmitField('Submit')
    