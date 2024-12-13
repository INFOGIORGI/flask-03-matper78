from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html",titolo="home")


@app.route("/details")
def detail():
    dati=((1,1,1),(2,2,2),(3,3,3))
    return render_template("detail.html",titolo="detail",dati=dati)

app.run(debug=True)

