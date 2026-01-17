from flask import Flask, redirect, url_for, render_template, request, session,flash
from datetime import timedelta
import sqlalchemy

app=Flask(__name__)
app.secret_key ="232jhdjhsdgfas"
app.permanent_session_lifetime =timedelta(minutes=10)

@app.route("/")
def home():
    return redirect(url_for("login"))

@app.route("/login",methods =["POST","GET"])
def login():
    if request.method =="POST":
        user = request.form.get("nm")
        session.permanent = True
        session["user"]=user
        flash("You have been logged in","sucess")
        return redirect(url_for("user"))
        
    else:
        if "user" in session:
            flash("You are already logged in","info")
            return redirect(url_for("user"))
        return render_template("login.html")

@app.route("/user",methods=["POST","GET"])
def user():
    email = None
    if "user" in session:
        user =session["user"] 
        if request.method== "POST":
            email=request.form.get("email")
            session["email"] = email

        else:
            if "email" in session:
                email = session["email"]
        return render_template("index.html",email=email,user=user)
    else:
        flash("You are not logged in","info")
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user",None)
    session.pop("email",None)
    flash(f"You have been logged out","info")
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)