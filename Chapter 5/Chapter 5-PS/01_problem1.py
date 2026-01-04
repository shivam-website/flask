from flask import Flask, redirect, url_for,render_template,request,session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "4545dfhsuidfhs8ufs8h3893%^$&*$(#@fhdskjfdksfnsdkjf8#*#($U(#*)))"
app.permanent_session_lifetime = timedelta(minutes=1)

@app.route("/")
def home():     
    return render_template("login.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        session.permanent = True
        user =request.form.get("nm")
        password =request.form.get("password")
        session["user"]=user
        return redirect(url_for("user"))
    else:
        if "user" in session:
            return redirect(url_for("user"))
    return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
        user = session["user"]
        return render_template("user.html", user=user)
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug =True,port=8000)
