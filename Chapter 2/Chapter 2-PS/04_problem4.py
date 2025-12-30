from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome! back to home page."

@app.route("/go-home")
def go_home():
    return redirect(url_for("home"))

if __name__=="__main__":
    app.run(debug=True)