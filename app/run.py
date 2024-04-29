
from flask import Flask, render_template, jsonify
from .modelli.models import Persona, Test
from .modelli.forms import testPostForm

# wtforms


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'



# route di default
@app.route("/persone")
def default():
    # simulazione di una serie di dati della classe selezionata 
    data = [Persona("John", "Doe"), Persona("Jane", "Doe"), Persona("Riccardo", "Tognetti"), Persona("Leonardo", "Brugnara")]
    
    # prende tutti gli attributi della classs di'interesse
    attribute_names = [attr for attr in dir(Persona("", "")) if not attr.startswith("__")]

    return render_template("home.html", data=data, attr=attribute_names)

@app.route("/test")
def getTest():
    # simulazione di una serie di dati della classe selezionata
    data = [Test("John", "Doe"), Test("Jane", "Doe"), Test("Riccardo", "Tognetti"), Test("Leonardo", "Brugnara")]

    # prende tutti gli attributi della classs di'interesse
    attribute_names = [attr for attr in dir(Test("", "")) if not attr.startswith("__")]
    
    return render_template("home.html", data=data, attr=attribute_names) 


@app.route("/forms", methods=['GET', 'POST'])
def forms():
    form = testPostForm()

    if form.validate_on_submit():
        name = form.nome.data
        return f"Hello, { name }!"

    return render_template("forms.html", form=form)