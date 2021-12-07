import os
import tabulate
import json
from flask import Flask, render_template
from pprint import pprint
app = Flask(__name__, static_url_path="")

jsonName = "project.json"
os.chdir("C:/Users/matte/Onedrive/Documenti/Project")
def unificaJson():
    lista = os.listdir()
    listaCartelle = []
    for x in lista:
        if not os.path.isfile(x):
            if controlloJson(x): 
                pathFile = x+"/"+jsonName
                file = open(pathFile, "r")
                fileJson = json.load(file)
                listaCartelle.append(fileJson)
    return listaCartelle

def controlloJson(cartella):
    listaFile = os.listdir(cartella)
    if jsonName in listaFile:
        return True
    else:
        return False

# sample = open("sample.json", "r")
# sampleJson = json.load(sample)
tuttiJson = unificaJson()
@app.route("/")
def index():
    return render_template("index.html", files = tuttiJson)



app.run(port=80, debug=False)