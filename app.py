from flask import Flask,render_template

app = Flask(__name__)
dati=(("Mammita","SC1",1),("Sierda","SC2",2),("Sorda","SC3",3))

@app.route("/")
def home():
    return render_template("home.html",titolo="home")


@app.route("/details")
def detail():
   
    return render_template("detail.html",titolo="detail",dati=dati)

@app.route("/scaffale/<nScaff>")
def scaffale(nScaff):
    lista=[]
    for i in dati:
        if i[1]==nScaff:
            lista.append(i)
    return render_template("scaffale.html",titolo="scaffale",lista=lista,nScaff=nScaff)

app.run(debug=True)

