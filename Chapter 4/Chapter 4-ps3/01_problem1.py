from flask import Flask,render_template,url_for
import pyjokes
import pyttsx3
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")
@app.route("/jokes")
def joke():
    engine = pyttsx3.init()

    generated_jokes =(pyjokes.get_joke())
    engine.say(generated_jokes)
    engine.setProperty('rate', 155)
    voices = engine.getProperty('voices') 
    engine.setProperty('voice', voices[1].id) 
    engine.runAndWait()     
    return render_template("base.html",jokes=generated_jokes)

if __name__=="__main__":
    app.run(debug=True)