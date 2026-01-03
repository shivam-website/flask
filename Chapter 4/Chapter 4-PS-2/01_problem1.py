from flask import Flask, redirect, url_for,render_template,request
import pyttsx3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("landing.html")

@app.route("/login",methods =["POST","GET"])
def login():
    if request.method=="POST":
        user = request.form.get("nm")
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/dashboard/<usr>")
def user(usr):
    tts_text = f"Welcome {usr}."

    return render_template(
        "main.html",
        usr=usr,
        tts_text=tts_text
    )


if __name__ == "__main__":
    app.run(debug =True)
