
from wtforms import Form, BooleanField, StringField, validators
from .models import Persona, Test

class newPersonaForm(Form):
    nome = StringField('nome', [validators.Length(min=2)])
    cognome = StringField('cognome', [validators.Length(min=2)])

class newTestForm(Form):
    name = StringField('name', [validators.Length(min=2)])
    surname = StringField('surname', [validators.Length(min=2)])

class interact_with_forms:

    #TODO: aggiungi in lowercase le classi che si vogliono interagire
    def getFormClasses():
        return {
            "persona": newPersonaForm,
            "test": newTestForm
        }