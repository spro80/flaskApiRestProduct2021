from flask import Flask, request
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import jsonify
from flask_cors import CORS, cross_origin

from flasgger import Swagger
from database import db
from models import Product

app = Flask(__name__)
CORS(app, support_credentials=True)
swagger = Swagger(app)

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
#db = SQLAlchemy(app)
db.init_app(app)

#Configurar flask-migrate
migrate = Migrate()
migrate.init_app(app, db)



def create_structure_product_list(product):
    product_list = []
    product_dict = {}
    for count,ele in enumerate(product,0):
        product_dict = {
            "id":ele.id,
            "sku":ele.sku,
            "name":ele.name,
            "price":ele.price,
            "brand":ele.brand,
            "stock":ele.stock,
        }
        product_list.append(product_dict)
    return product_list



@app.route('/product/list')
@cross_origin(supports_credentials=True)
def products_list():
    """
    Endpoint returning a list of products.
    This is using docstrings for specifications.
    ---
    responses:
      200:
        code: 200,
        description: A list of products
    """
    product = Product.query.all()
    total_products = Product.query.count()

    prod_list = []
    prod_list = create_structure_product_list(product) 
    
    response = {
        'status': 'ok',
        'code': 200,
        'data': prod_list
    }
    return jsonify( response )



@app.route('/product/view/<int:id>')
@cross_origin(supports_credentials=True)
def view_details( id ):
    """
    Endpoint returning details of product by id.
    This is using docstrings for specifications.
    ---
    parameters:
      - name: id
        in: path
        type: int
        required: true
    responses:
      200:
        code: 200,
        description: All data of product by id
    """
    product = Product.query.get( id )
    if product is None:
        response = {
            'status': 'ok',
            'code': 200,
            'description': 'product not found',        
        }
        return jsonify( response )
    #app.loger.debug(f'view product: {producto}')
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



@app.route('/product/add', methods=['POST'])
@cross_origin(supports_credentials=True)
def add():
    """
    Endpoint add product.
    This is using docstrings for specifications.
    ---
    responses:
      200:
        code: 200,
        description: Add product in database
    """
    if request.method == 'POST':
        data = request.get_json()
        req_sku = data["sku"]
        req_name = data["name"]
        req_price = data["price"]
        req_brand = data["brand"]
        req_stock = data["stock"]
        new_product = Product(sku=req_sku, name=req_name, price=req_price, brand=req_brand, stock=req_stock )
        db.session.add(new_product)
        db.session.commit()
        response = {
            'status': 'ok',
            'code': 200,
            'description': 'add product is ok',
        }
        response.headers.add("Access-Control-Allow-Origin", "*")
        return jsonify( response )

@app.route('/product/delete/<int:id>', methods=['DELETE'])
@cross_origin(supports_credentials=True)
def delete_product(id):
    """
    Endpoint delete product by id.
    This is using docstrings for specifications.
    ---
    parameters:
      - name: id
        in: path
        type: int
        required: true
    responses:
      200:
        code: 200,
        description: Delete product by id
    """
    if request.method == 'DELETE':
        product = Product.query.get( id )
        if product is None:
            response = {
                'status': 'ok',
                'code': 200,
                'description': 'The product is not exist in Database',        
            }
            return jsonify( response )
        delete_product_id = id
        x = db.session.query(Product).get( delete_product_id )
        db.session.delete(x)
        db.session.commit()
        response = {
            'status': 'ok',
            'code': 200,
            'description': 'The product was deleted correctly',
        }
        return jsonify( response )


@app.route('/product/edit', methods=['POST'])
@cross_origin(supports_credentials=True)
def edit_product():
    """
    Endpoint edit data of product by id.
    This is using docstrings for specifications.
    ---
    responses:
      200:
        code: 200,
        description: Edit product by id
    """
    data = request.get_json()
    product_id = data["id"]
    if request.method == 'POST':
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
