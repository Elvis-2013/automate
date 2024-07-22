from flask import Flask
import os

app = Flask(__name__)

@app.route("/")

def home():
    return "elvis automation sms app"

if __name__ == '__main__':
    app.run(debug=True)
