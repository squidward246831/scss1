import flask from flask, render_template

app=flask(__name__)

@app.route("/hello")
def index(""):
    return render_template=("index.html")
