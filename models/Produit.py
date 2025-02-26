from config import db
class Produit(db.Model):
    __tablename__ = 'produits'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    description = db.Column(db.String())
    price = db.Column(db.Integer())
    qte = db.Column(db.Integer())
    image = db.Column(db.String())

    def __init__(self, name, description, price, qte, image):
        self.name = name
        self.description = description
        self.price = price
        self.qte = qte
        self.image = image

    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "qte": self.qte,
            "image": self.image
        }

    
    def __repr__(self):
        return f"<Produit {self.name}>"