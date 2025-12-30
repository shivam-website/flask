from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome! back to home page."

@app.route("/skills/<name>")
def skills(name):
    return render_template("05_index.html",skills = ["Python", "Flask", "HTML"],content=name)

if __name__=="__main__":
    app.run(debug=True)