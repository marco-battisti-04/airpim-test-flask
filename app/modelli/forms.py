
'''from flask_wtf import FlaskForm
from wtforms import Form, BooleanField, StringField, validators, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length'''

from wtforms import Form, BooleanField, StringField, validators
from .models import Persona, Test

class testPostForm(Form):
    nome = StringField('nome', [validators.Length(min=2)])


# TODO: vedere se è possibile fare tutto con una sola classe in modo dinamico
# possibile creazione di un unica classe form e prendere solo i campi voluti
class newPersonaForm(Form):
    nome = StringField('nome', [validators.Length(min=2)])
    cognome = StringField('cognome', [validators.Length(min=2)])

class newTestForm(Form):
    name = StringField('name', [validators.Length(min=2)])
    surname = StringField('surname', [validators.Length(min=2)])



class interact_with_forms:

    # aggiungi in lowercase le classi che si vogliono interagire
    def getFormClasses():
        return {
            "persona": newPersonaForm,
            "test": newTestForm
        }