from flask import Flask, redirect, request, jsonify, escape
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
    base_url = "http://104.236.34.0/getinfo?"

    def _reqargs(arg):
        return request.args.get(arg)
    # strength
    power = _reqargs("power")
    toughness = _reqargs("toughness")
    color = _reqargs("color")
    loyalty = _reqargs("loyalty")
    text = _reqargs("text")


    card_collection = CardCollection()
    strength_results = []

    full_url = base_url

    if power or toughness:
        strength_arg = ""
        if power:
            full_url += "power=" + power + "&"
        if toughness:
            full_url += "toughness=" + toughness + "&"

    if color:
        full_url +=  "color=" + color + "&"

    if loyalty:
        full_url += "loyalty=" + loyalty + "&"

    if text:
        from requests.utils import quote
        full_url += "text=" + quote(text)

    full_url = full_url.rstrip("&")

    app.logger.info("URL to use to query web service api: {}".format(full_url))
    res = requests.get(full_url)
    app.logger.info("Status code returned for web service api query: {}".format(res.status_code))
    json_data = res.json()
    cards = json_data.get("results")

    return jsonify({"results":cards})

if __name__ == "__main__":
    app.run(debug=True)