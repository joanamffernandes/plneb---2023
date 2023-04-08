from flask import Flask, render_template

# app = Flask(__name__)

app = Flask(__name__, static_url_path='/imagens', static_folder='imagens')


@app.route("/")
def menu():
    return  render_template('menu.html')


@app.route("/engenharia")
def engenharia():
    return  render_template('engenharia.html')


@app.route("/elefante")
def elefante():
    return  render_template('elefante.html')


@app.route("/egua")
def egua():
    return  render_template('egua.html')

app.run(host="localhost", port=3000, debug=True)