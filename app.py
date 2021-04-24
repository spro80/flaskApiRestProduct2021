from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify

app = Flask(__name__)



@app.route("/")
def index():
    return "Healtcheck Get in /"



#postgres://fsfaoylpyzrhos:76e5730bcb1ea339a54979203d2d7ec5e43f587fcdd9f0dd96162c0404a85792@ec2-34-225-167-77.compute-1.amazonaws.com:5432/dfndduigsrotgr
USER_DB = 'fsfaoylpyzrhos'
PASS_DB = '76e5730bcb1ea339a54979203d2d7ec5e43f587fcdd9f0dd96162c0404a85792'
URL_DB = 'ec2-34-225-167-77.compute-1.amazonaws.com:5432'
NAME_DB = 'dfndduigsrotgr'
FULL_URL_DB = f'postgresql://{USER_DB}:{PASS_DB}@{URL_DB}/{NAME_DB}'

app.config['SQLALCHEMY_DATABASE_URI'] = FULL_URL_DB
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializacion del objeto db de sqlalchemy
db = SQLAlchemy(app)

#Configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sku = db.Column(db.String(250))
    name = db.Column(db.String(250))
    price = db.Column(db.Integer)
    brand = db.Column(db.String(250))
    stock = db.Column(db.Integer)

    def __str__(self):
        return(
            f'Id: {self.id, }'
            f'sku: {self.sku, }'
            f'name: {self.name, }'
            f'price: {self.price, }'
            f'brand: {self.brand, }'
            f'stock: {self.stock}'
        )




@app.route('/product/list')
def products_list():
    print('Init in products_list')
    response = {
        'status': 'ok'
    }
    return jsonify( response )


@app.route('/product/view/<int:id>')
def view_details( id ):
    print('Init in view_details')
    # Recuperamos la fila de acuerdo al id consultado.
    product = Product.query.get( id )

    if product is None:
        return 'No se han encontrado datos'
    #app.loger.debug(f'Ver persona: {producto}')
    response = {
    'status': 'ok',
    'code': 200,
    'description': 'response ok',
    'data': {
        'sku':product.sku,
        'name':product.name,
        'price':product.price,
        'brand':product.brand,
        'stock':product.stock
    }
    }
    return jsonify( response )


@app.route('/product/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        #req_id = data["id"]
        req_sku = data["sku"]
        req_name = data["name"]
        req_price = data["price"]
        req_brand = data["brand"]
        req_stock = data["stock"]
        print(f"req_stock: {req_stock}")
        new_product = Product(sku=req_sku, name=req_name, price=req_price, brand=req_brand, stock=req_stock )
        db.session.add(new_product)
        db.session.commit()
        print("add new row")
        response = {
            'status': 'ok',
            'code': 200,
            'description': 'add product is ok',
        }
        return jsonify( response )


@app.route('/product/delete', methods=['GET', 'POST'])
def delete_product():
    if request.method == 'POST':
        data = request.get_json()
        print(data)
        delete_product_id = data["id"]
        x = db.session.query(Product).get( delete_product_id )
        db.session.delete(x)
        db.session.commit()
        response = {
            'status': 'ok',
            'code': 200,
            'description': 'The product was deleted correctly',
        }
        return jsonify( response )


@app.route('/product/edit', methods=['GET', 'POST'])
def edit_product():
    data = request.get_json()
    product_id = data["id"]
    print(f'product_id: {product_id}')
    if request.method == 'POST':
        print(data["sku"])
        x = db.session.query(Product).get( product_id )
        x.sku = data["sku"]
        x.name = data["name"]
        x.price = data["price"]
        x.brand = data["brand"]
        x.stock = data["stock"]
        db.session.commit()
        response = {
            'status': 'ok',
            'code': 200,
            'description': 'The product was edited correctly',
        }
        return jsonify( response )
