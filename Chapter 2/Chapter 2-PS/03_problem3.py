from flask import Flask, redirect, url_for,render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template("03_index.html",marks = [45, 72, 88, 60])

if __name__ == "__main__":
    app.run(debug =True)
