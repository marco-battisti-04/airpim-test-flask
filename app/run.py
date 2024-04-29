###########
# IMPORTS #
###########
from flask import Flask, render_template,url_for, redirect, request
from .modelli.models import Persona, Test
from .modelli.forms import testPostForm

# APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'




##########
# ROUTES #
##########

# default
@app.route("/")
def default():
    return redirect(url_for("persone"))

# get / persone
@app.route("/persone")
def persone():
    # simulazione di una serie di dati della classe selezionata 
    data = [Persona("John", "Doe"), Persona("Jane", "Doe"), Persona("Riccardo", "Tognetti"), Persona("Leonardo", "Brugnara")]
    
    # prende tutti gli attributi della classs di'interesse
    attribute_names = [attr for attr in dir(Persona("", "")) if not attr.startswith("__")]

    return render_template("home.html", data=data, attr=attribute_names)

# get / test
@app.route("/test")
def getTest():
    # simulazione di una serie di dati della classe selezionata
    data = [Test("John", "Doe"), Test("Jane", "Doe"), Test("Riccardo", "Tognetti"), Test("Leonardo", "Brugnara")]

    # prende tutti gli attributi della classs di'interesse
    attribute_names = [attr for attr in dir(Test("", "")) if not attr.startswith("__")]
    
    return render_template("home.html", data=data, attr=attribute_names) 

# post / forms
@app.route("/forms", methods=['GET', 'POST'])
def forms():
    form = testPostForm(request.form)

    if request.method == 'POST' and form.validate():
        print(form.nome.data)
        return redirect(url_for("persone"))

    return render_template("forms.html", form=form)