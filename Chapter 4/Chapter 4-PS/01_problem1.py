from flask import Flask, redirect, url_for,render_template,request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/login",methods =["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/skills/<usr>")
def user(usr):
    return render_template("skills.html",skills = ["Python", "Flask", "HTML", "CSS"],usr=usr)

if __name__ == "__main__":
    app.run(debug =True)
