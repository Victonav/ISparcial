from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return "Taylor Swift, Fearless, Speak Now (TV), Red(TV), 1989, Rep, Folklore, Evermore, Midnights"

if __name__ == "__main__": 
    app.run()