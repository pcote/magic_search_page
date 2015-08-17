from flask import Flask, redirect, request
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/static/index.html")

@app.route("/getinfo", methods=["GET"])
def get_info():
    return "Nothing"

if __name__ == "__main__":
    app.run(debug=True)