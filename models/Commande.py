from config import db

class Commande(db.Model):
    __tablename__ = 'commandes'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    details = db.relationship('DetailCommande', backref='commande', lazy=True)
    # liste de detail de commande
    



    def __init__(self, produit_id, user_id):
        self.produit_id = produit_id
        self.user_id = user_id

    def __repr__(self):
        return f"<Commande {self.id}>"