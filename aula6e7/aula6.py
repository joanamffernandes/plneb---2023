from flask import Flask, render_template
import json

app = Flask(__name__)

file = open("dicionario_traduzido.json", encoding="utf8")

db = json.load(file)

@app.route("/")

def hello_world():

    return  render_template('inicio.html', title="Welcome!!")

@app.route("/terms")
def terms():
    return  render_template('terms.html', designations=db.keys())


@app.route("/term/<t>")
def term(t):
    return  render_template('term.html', designation=t, value= db.get(t, "None"))


app.run(host="localhost", port=3000, debug=True)