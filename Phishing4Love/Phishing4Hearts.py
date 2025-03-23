import flask
from flask import render_template
import random as rand


app = flask.Flask(__name__)
@app.route("/")
def index():
    emails = {"uah.college@gmail.com": True,"apple@gmail.com": True, "Totallyfake@gmail.com": False, "To2389@uah.edu": False, "admin@uah.edu": False }
    x = rand.choice( list(emails.keys()))
    Age = rand.randint(18, 100)
    return render_template("Phishing.html", emails=emails, Age = Age)
app.run(host="0.0.0.0", port=80)
 
