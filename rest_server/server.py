"""This module contains only the REST handlers."""
from flask import Flask, jsonify, request
from rest_server.menu_handler import process_menu

app = Flask(__name__)


@app.route('/ping')
def ping():
    """The client pings the server to know whether or not it is connected."""
    return jsonify(message="Gutlic's Arena Server version 1.0")


@app.route('/new_game', methods=['POST'])
def new_game_handler():
    """Goes through the steps of creating a new character and game."""
    state = request.json['state']
    if 'item' in request.json:
        item = request.json['item']
    else:
        item = ''
    if 'menu_id' in request.json:
        menu_id = request.json['menu_id']
    else:
        menu_id = 'new_game'
    return jsonify(process_menu(menu_id, item, state))


app.run(debug=True)