
from flask import Flask, render_template, jsonify

# FIXME: 1) risolvere problema del modello non trovato
# from modelli.models import Persona 

app = Flask(__name__)

# route di default
@app.route("/persone")
def default():

    data = [Persona("John", "Doe"), Persona("Jane", "Doe"), Persona("Riccardo", "Tognetti"), Persona("Leonardo", "Brugnara")]
    
    attribute_names = [attr for attr in dir(Persona("", "")) if not attr.startswith("__")]
    
    return render_template("home.html", data=data, attr=attribute_names)

@app.route("/test")
def getTest():

    data = [Test("John", "Doe"), Test("Jane", "Doe"), Test("Riccardo", "Tognetti"), Test("Leonardo", "Brugnara")]
    # people = Test("John", "Doe")

    # prende tutti gli attributi della classs di'interesse
    attribute_names = [attr for attr in dir(Test("", "")) if not attr.startswith("__")]
    
    return render_template("home.html", data=data, attr=attribute_names) 

#FIXME: 2) spostare le righe seguenti in models.py appena risolto il fixme precedente

class Persona:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


class Test:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname