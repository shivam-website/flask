from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)
@app.route("/<name>")
def home(name):
    return render_template("native_python.html",content=[name,"class 9","begginer"])

if __name__ == "__main__":
    app.run(debug =True)
