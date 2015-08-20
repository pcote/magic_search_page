from flask import Flask, redirect, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return redirect("/static/index.html")

@app.route("/lookupcards", methods=["GET"])
def get_info():
    base_url = "http://104.236.34.0/"

    def _reqargs(arg):
        return request.args.get(arg)
    # strength
    power = _reqargs("power")
    toughness = _reqargs("toughness")
    color = _reqargs("color")
    loyalty = _reqargs("loyalty")

    strength_results = []
    if power or toughness:
        strength_arg = "strength?"
        if power:
            strength_arg = strength_arg + "power=" + power + "&"
        if toughness:
            strength_arg = strength_arg + "toughness=" + toughness

        strength_arg = strength_arg.rstrip("&")
        full_url = base_url + strength_arg
        print(full_url)
        strength_results = requests.get(full_url).json().get("results")


    card_list = strength_results
    print(card_list)
    return jsonify({"results":card_list})

if __name__ == "__main__":
    app.run(debug=True)