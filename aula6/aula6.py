from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")

def hello_world():
    return  render_template('inicio.html', title="home")

@app.route("/home")
def home():
    return  render_template('home.html', title="home")


@app.route("/creditos")
def creditos():
    return  render_template('creditos.html', title="creditos")

app.run(host="localhost", port=3000, debug=True)