from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)


#postgres://fsfaoylpyzrhos:76e5730bcb1ea339a54979203d2d7ec5e43f587fcdd9f0dd96162c0404a85792@ec2-34-225-167-77.compute-1.amazonaws.com:5432/dfndduigsrotgr
USER_DB = 'fsfaoylpyzrhos'
PASS_DB = '76e5730bcb1ea339a54979203d2d7ec5e43f587fcdd9f0dd96162c0404a85792'
URL_DB = 'ec2-34-225-167-77.compute-1.amazonaws.com:5432'
NAME_DB = 'dfndduigsrotgr'
FULL_URL_DB = f'postgres://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializacion del objeto db de sqlalchemy
db = SQLAlchemy(app)

#Configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)



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