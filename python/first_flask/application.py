from flask import Flask, render_template

app = Flask(__name__)


@app.route("/") 
def index():
    headline="This is the headline!"
    return render_template("index.html", headline=headline) # render template seems to need a templates directory

@app.route("/david")
def david():
    return "Hello, David"

@app.route("/<string:name>") #route captures any name now
def hello(name):
    name = name.capitalize()
    return f"hello, {name}!"