from flask import Flask
from flask import jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return "Healtcheck Get in /"


@app.route('/product/list')
def products_list():
    print('Init in products_list')
    response = {
        'status': 'ok'
    }
    return jsonify( response )