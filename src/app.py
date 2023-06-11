from flask import Flask

app= Flask(__name__)

@app.route("/")
def index():
    return "Taylor Swift, Fearless(TV), Speak Now (TVS), Red(TV), 1989(TV), Rep, Folklore, Evermore, Midnights"

if __name__ == "__main__": 
    app.run()