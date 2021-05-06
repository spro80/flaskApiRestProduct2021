from app import db

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
