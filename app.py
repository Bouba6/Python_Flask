from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from templates.FormType.productForm import ProductForm
from models.Produit import Produit
from models.User import User
from models.Commande import Commande
from models.DetailCommande import DetailCommande
from flask import jsonify,session,request
from config import app, db
from werkzeug.utils import secure_filename
import os

# Flask-Migrate for database migrations
migrate = Migrate(app, db)

UPLOAD_FOLDER = 'static/images'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


#faire aussi que le index prend un parametre une donnee de recherche ou rien

@app.route("/")
def home():
        return render_template("Home/index.html",products=Produit.query.all())

@app.route("/about") 
def about():
        return render_template("About/index.html")

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/search/<search>")
def search(search):
    # Récupérer les produits qui correspondent à la recherche
    products = Produit.query.filter(Produit.name.ilike("%" + search + "%")).all()
    # Convertir les produits en JSON
    data = [{"id": p.id, "name": p.name ,"description": p.description, "price": p.price, "qte": p.qte, "image": p.image} for p in products]
    # Retourner les données en JSON
    return jsonify(data)

@app.route("/service")
def service():
        return render_template("Service/index.html")

@app.route("/addtocart/<int:productId>", methods=["POST"])
def add_to_cart(productId):
    try:
        # Crée le panier dans la session s'il n'existe pas
        if "cart" not in session:
            session["cart"] = []
        
        # Recherche du produit
        produit = Produit.query.filter_by(id=productId).first()
        if produit is None:
            return jsonify({"error": "Produit non trouvé"}), 404
        
        # Ajoute le detialCommande sérialisé au panier
        ajouterProduit(produit,1)
        
        return jsonify({"message": "Produit ajouté au panier"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
        

def ajouterProduit(produit,qte):
    # Crée le panier dans la session s'il n'existe pas
    if "cart" not in session:
        session["cart"] = []
    
    # Ajoute le produit au panier
    produitserialized = produit.serialize()
    detail_commande = DetailCommande(
        commande_id=None,  # ou une valeur appropriée si vous avez un identifiant de commande
        produit_id=produitserialized.get("id"),
        qte=qte
    ).serialize()
    
    session["cart"].append(detail_commande)
    session.modified = True  # Indique à Flask que la session a changé    
    
@app.route("/cart")
def show_cart():
    if "cart" in session:
        return render_template("Commande/form.html",products=session["cart"])

@app.route("/destroycart")
def destroy_cart():
    if "cart" in session:
        del session["cart"]
    return redirect("/cart")

def prixTotal():
    total = 0
    if "cart" in session:
        for detail_commande in session["cart"]:
            produit = Produit.query.filter_by(id=detail_commande["produit_id"]).first()
            total += produit.price * detail_commande["qte"]
    return total

@app.route("/update/<int:productId>", methods=["POST"])
def update(productId):
    try:
        # Crée le panier dans la session s'il n'existe pas
        if "cart" not in session:
            session["cart"] = []
        
        # Recherche du produit dans la session
        produit = next((p for p in session["cart"] if p["produit_id"] == productId), None)
        if produit is None:
            return jsonify({"error": "Produit non trouvé dans le panier"}), 404
        
        # Mettre à jour la quantité du produit dans la session
        produit["qte"] = request.json.get("qte", produit["qte"])
        session.modified = True  # Indique à Flask que la session a changé
        Total=prixTotal()
        return jsonify({"message": "Quantité mise à jour","total":Total})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
   
@app.route("/add_product",)
def add_product():
        form=ProductForm()
        return render_template("Home/form.html",form=form)

@app.route('/submit', methods=['GET', 'POST'])
def submit():
    form = ProductForm()
    if form.validate_on_submit():
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        produit=Produit(form.name.data,form.description.data,form.price.data,form.qte.data,filename)
        db.session.add(produit)
        db.session.commit()
        return render_template("Home/index.html",products=Produit.query.all())
    return render_template('Home/form.html', form=form)





# @app.route("/hello")
# @app.route("/hello/<name>")
# def hello_name(name):
#         #changer le nom modifier genre si y'a i on le remplace par y
#         name=name.replace("i","y")  
#         return render_template("hello.html",person=name)


# @app.route("/hello/<int:score>")
# def hello_score(score):
#         return f"<p>Sa slip mame { score }</p>"

# def create_app():