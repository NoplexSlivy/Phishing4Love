import flask
from flask import render_template
import requests

emails = {"uah.college@gmail.com": True,"apple@gmail.com": True, "Totallyfake@gmail.com": False, "To2389@uah.edu": False, "admin@uah.edu": False }
app = flask.Flask(__name__)

@app.route("/")
def index():
    return render_template("Phishing.html")
app.run(host="0.0.0.0", port=80)
 
