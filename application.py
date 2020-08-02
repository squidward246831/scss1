from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/PASSWORD", methods=["POST"])
def hello():
    name = request.form.get("name")
    return render_template("hello.html", name=name)

@app.route("/Correct", methods=["POST","get"])
def correct():
    number=request.form.get("number")
    return render_template("correct.html", number=number)
    if name > advay:
        return 'correct'
@app.errorhandler(405)
def four0five_handler(error):
    return render_template("error.html"), 405
@app.errorhandler(404)
def four0four_handler(error):
    return render_template("error2.html"), 404
