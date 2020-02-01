from flask import Flask, jsonify
import json

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify(message="Gutlic's Arena Server version 1.0")


@app.route('/new_game')
def new_game_handler():
    # load the new_game template and fill in the choices if necessary
    new_game = json.load(open('rest_server/resources/new_game.json'))
    return jsonify(new_game)
