import flask
from flask import render_template
import requests
import random as rand


app = flask.Flask(__name__)

@app.route("/")
def index():
    x = rand.choice( list(emails.keys()))
    Age = rand.randint(18,68)
    emails = {"uah.college@gmail.com": True,"apple@gmail.com": True, "Totallyfake@gmail.com": False, "To2389@uah.edu": False, "admin@uah.edu": False }
    return render_template("Phishing.html", Age=Age, ranemail=x, emails=emails)
app.run(host="0.0.0.0", port=80)
 
