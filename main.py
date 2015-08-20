from flask import Flask, redirect, request, jsonify
import requests

class CardCollection(object):
    def __init__(self):
        self._queue = []

    def update_queue(self, new_data):
        if len(self._queue) == 0:
            self._queue = new_data
            return

        self._queue = [card for card in self._queue
                        if card.get("name") in [card.get("name") for card in new_data]]

    @property
    def collection(self):
        return self._queue

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

    card_collection = CardCollection()
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
        card_collection.update_queue(strength_results)

    if color:
        full_url = base_url + "color?color=" + color
        results = requests.get(full_url)
        results = requests.get(full_url).json().get("results")
        card_collection.update_queue(results)

    if loyalty:
        full_url = base_url + "loyalty/" + loyalty
        results = requests.get(full_url)
        results = requests.get(full_url).json().get("results")
        card_collection.update_queue(results)


    print(card_collection.collection)
    return jsonify({"results":card_collection.collection})

if __name__ == "__main__":
    app.run(debug=True)