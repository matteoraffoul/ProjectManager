import os
import json
from flask import Flask, render_template
app = Flask(__name__, static_url_path="")

jsonName = "project.json"
workingPath = "C:/Users/matte/Onedrive/Documenti/Project"
#workingPath = input("Inserisci il percorso dove sono presenti i progetti: ")
os.chdir(workingPath)
def unificaJson():
    lista = os.listdir()
    listaCartelle = []
    for x in lista:
        if not os.path.isfile(x):
            if controlloJson(x): 
                pathFile = x+"/"+jsonName
                with open(pathFile) as file:
                    fileJson = json.load(file)
                fileJson["path"] = workingPath + "/" + x
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



app.run(port=80, debug=True)