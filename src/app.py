from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return "Taylor Swift(TV), Fearless(TV), Speak Now (TV), Red(TV), 1989, Rep(TV), Folklore, Evermore, Midnights"

if __name__ == "__main__": 
    app.run()