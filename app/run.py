###########
# IMPORTS #
#region ###

from flask import Flask, render_template,url_for, redirect, request
from json import JSONEncoder
from .modelli.models import Persona, Test
from .modelli.forms import testPostForm, interact_with_forms
from .modelli import models

import inspect
import json
##############
# END ROUTES #
#endregion ###

# APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# simulazione di dati
testList = [Test("John", "Doe"), Test("Jane", "Doe"), Test("Riccardo", "Tognetti"), Test("Leonardo", "Brugnara")]
personeList = [Persona("John", "Doe"), Persona("Jane", "Doe"), Persona("Riccardo", "Tognetti"), Persona("Leonardo", "Brugnara")]

class_list_mapping = {
    "persona": personeList,
    "test": testList
}

##########
# ROUTES #
#region ##

# default
@app.route("/")
def default():
    return redirect(url_for("persona"))

# get / persone
@app.route("/persona")
def persona():

    # prende tutti gli attributi della classs di'interesse
    attribute_names = [attr for attr in dir(Persona("", "")) if not attr.startswith("__")]
    add_text = "aggiungi a persona"
    add_link = "persona"

    return render_template("home.html", data=personeList, attr=attribute_names, addtext=add_text, addink=add_link)

# get / test
@app.route("/test")
def getTest():

    # prende tutti gli attributi della classs di'interesse
    attribute_names = [attr for attr in dir(Test("", "")) if not attr.startswith("__")]
    add_text = "aggiungi a test"
    add_link = "persona"

    return render_template("home.html", data=testList, attr=attribute_names, addtext=add_text, addink=add_link)

# get & post / forms
@app.route("/forms/<form_class>", methods=['GET', 'POST'])
def forms(form_class):

    class_names = [obj for obj in dir(models) if inspect.isclass(getattr(models, obj))]

    form_name = form_class.lower()
    attribute_names = []
    for class_name in class_names:
        if form_name in class_name.lower():
            class_obj = globals()[class_name]
            attribute_names = [attr for attr in dir(class_obj) if not attr.startswith("__")]

    classes_list = interact_with_forms.getFormClasses()
    form_classes = classes_list.get(form_name)
    form = form_classes(request.form)
    fields = attribute_names

    # POST REQUSET
    if request.method == 'POST' and form.validate():
        jsondata = json.dumps(form.data)
        python_obj = json.loads(jsondata)

        # cerca la classe giusta
        current_class = ""
        for class_name in class_names:
            if form_name in class_name.lower():

                # crea un nuovo oggetto
                current_class = class_name
                myclass = globals()[class_name]
                final_obj = myclass(**python_obj)

        # salva l'oggetto sulla sua lista
        class_list_mapping[current_class.lower()].append(final_obj)
        return redirect(url_for(str(current_class.lower())))

    return render_template("forms.html", form=form, fields=fields)

##############
# END ROUTES #
#endregion ###

class MyClass:
    def __init__(self, name, age):
        self.name = name
        self.age = age
