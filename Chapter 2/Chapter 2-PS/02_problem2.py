from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)
@app.route("/welcome/<name>")
def welcome(name):
    return render_template("02_index.html",content=name)

if __name__ == "__main__":
    app.run(debug =True)
