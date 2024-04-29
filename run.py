# Flask
# import os
from flask import Flask, render_template, jsonify

# Models

# FIXME: 1) risolvere problema del modello non trovato
# from modelli.models import Persona 

app = Flask(__name__)

# route di default
@app.route("/")
def default():
    # la cartella di default per i file è templates
    people = [Persona("John", "Doe"), Persona("Jane", "Doe"), Persona("Riccardo", "Tognetti"), Persona("Leonardo", "Brugnara")]
    cols = ["nome", "cognome"]
    # attribute_names = [attr for attr in dir(Persona("", "")) if not attr.startswith("__")]
    
    return render_template("home.html", people=people, cols=cols)

@app.route("/api/test")
def getTest():

    pass
    # Convert the dictionary to JSON using jsonify

#FIXME: 2) spostare le righe seguenti in models.py appena risolto il fixme precedente

class Persona:

    def __init__(self, nome, cognome):
        self.nome = nome
        self.cognome = cognome


class Test:

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname