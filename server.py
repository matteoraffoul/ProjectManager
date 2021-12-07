from flask import Flask, render_template
import json
app = Flask(__name__, static_url_path="")
allora = [{'element': 'Quadrato', 'file': False}, {'element': 'start.bat', 'file': True}, {'element': 'test.c', 'file': True}, {'element': 'test.exe', 'file': True}, {'element': 'Triangolo', 'file': False}]
sample = open("sample.json", "r")
sampleJson = json.load(sample)

@app.route("/")
def index():
    return render_template("index.html", files = sampleJson)



app.run(port=80, debug=True)