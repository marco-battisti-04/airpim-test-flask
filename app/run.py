###########
# IMPORTS #
#region ###

from flask import Flask, render_template,url_for, redirect, request
from json import JSONEncoder
from .modelli.models import Persona, Test
from .modelli.forms import  interact_with_forms
from .modelli import models

import inspect
import json
import sqlite3

##############
# END IMPORTS #
#endregion ###

# APP
app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# simulazione di dati
testList = [Test("John", "Doe"), Test("Jane", "Doe"), Test("Riccardo", "Tognetti"), Test("Leonardo", "Brugnara")]
personeList = [Persona("John", "Doe"), Persona("Jane", "Doe"), Persona("Riccardo", "Tognetti"), Persona("Leonardo", "Brugnara")]

# mappa delle liste per far capire all'interfaccia quale lista confrontare
class_list_mapping = {
    "persona": personeList,
    "test": testList
}

############
# DATABASE #
#region ####

def get_db_connection():
    conn = sqlite3.connect('app/database/database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_all_from_tables(table_name):
    conn = get_db_connection()
    cursor = conn.cursor()
    rows = cursor.execute('SELECT * FROM {table_name}').fetchall()

    data = []
    for row in rows:
        data.append(dict(zip([col[0] for col in cursor.description], row)))

    json_data = json.dumps(data)
    print(json_data)

    conn.close()
    return json_data


# get_all_from_tables()
################
# END DATABASE #
#endregion #####

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
def test():

    # prende tutti gli attributi della classs di'interesse
    attribute_names = [attr for attr in dir(Test("", "")) if not attr.startswith("__")]
    add_text = "aggiungi a test"
    add_link = "persona"

    return render_template("home.html", data=testList, attr=attribute_names, addtext=add_text, addink=add_link)

# get & post / forms
@app.route("/forms/<wanted_form_class>", methods=['GET', 'POST'])
def forms(wanted_form_class):
    # prende tutti i nomi di tutti i modelli
    class_names = [obj for obj in dir(models) if inspect.isclass(getattr(models, obj))]

    # prende il nome della classe passata come parametro e la mette in lowercase
    wanted_form_name = wanted_form_class.lower()

    # cerca il nome della classe selezionato tra i modelli
    attribute_names = []
    for class_name in class_names:
        if wanted_form_name in class_name.lower():
            class_obj = globals()[class_name]

            # prende i suoi attributi
            attribute_names = [attr for attr in dir(class_obj) if not attr.startswith("__")]

    # prende i le varie possibilita per la creazione del form in base al modello
    classes_list = interact_with_forms.getFormClasses()
    form_classes = classes_list.get(wanted_form_name)
    form = form_classes(request.form)
    fields = attribute_names

    # POST REQUSET
    if request.method == 'POST' and form.validate():
        jsondata = json.dumps(form.data)
        python_obj = json.loads(jsondata)

        # cerca la classe giusta
        current_class = ""
        for class_name in class_names:
            if wanted_form_name in class_name.lower():

                # crea un nuovo oggetto
                current_class = class_name
                myclass = globals()[class_name]
                final_obj = myclass(**python_obj)

        # salva l'oggetto sulla sua lista
        class_list_mapping[current_class.lower()].append(final_obj)
        return redirect(url_for(str(current_class.lower())))

    return render_template("forms.html", form=form, fields=fields)

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500

@app.errorhandler(404)
def page_not_found(e):
    return render_template('./errors/404.html'), 404

##############
# END ROUTES #
#endregion ###


