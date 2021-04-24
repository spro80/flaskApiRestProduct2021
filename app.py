from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Healtcheck Get in /"


@app.route('/product/list')
def products_list():
    print('Init in products_list')
    return 'Return all products !!!'