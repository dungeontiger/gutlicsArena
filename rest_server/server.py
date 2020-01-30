from flask import Flask
app = Flask(__name__)


@app.route('/ping')
def ping():
    return '{ "message": "Gutlic\'s Server 0.1"}'
