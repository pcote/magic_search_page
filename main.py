from flask import Flask, redirect, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/static/index.html")

@app.route("/lookupcards", methods=["GET"])
def get_info():
    results = [
        dict(name="Applejack", type="Pony Creature", rarity="Common", artist="Lauren Faust", set_name="Magic 2015")
    ]
    return jsonify({"results":results})

if __name__ == "__main__":
    app.run(debug=True)