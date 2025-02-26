from config import db

class DetailCommande(db.Model):
    __tablename__ = 'detail_commandes'
    id = db.Column(db.Integer, primary_key=True)
    commande_id = db.Column(db.Integer, db.ForeignKey('commandes.id'), nullable=False)
    produit_id = db.Column(db.Integer, db.ForeignKey('produits.id'), nullable=False)
    qte = db.Column(db.Integer())

    def __init__(self, commande_id, produit_id, qte):
        self.commande_id = commande_id
        self.produit_id = produit_id
        self.qte = qte

    def __repr__(self):
        return f"<DetailCommande {self.id}>"
    
    def serialize(self):
        return {
            "id": self.id,
            "commande_id": self.commande_id,
            "produit_id": self.produit_id,
            "qte": self.qte
        }