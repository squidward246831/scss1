from flask import Flask, render_template, request

app = Flask(__name__)




@app.route("/")
def index():
    return render_template("layout.html")

@app.route("/hello", methods=["POST"])
def hello():
    name = request.form.get("name")
    email = request.form.get("email")
    thought = request.form.get("thought")
    date = request.form.get("date")
    return render_template("hello.html", name=name, email=email, thought=thought, date=date)
