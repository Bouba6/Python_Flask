from flask_wtf import FlaskForm
from wtforms import StringField, FileField
from wtforms.validators import  Length

class ProductForm(FlaskForm):
    name = StringField('name', validators=[ Length(min=10, max=20, message="Le nom doit contenir entre 2 et 20 caractères")], render_kw={"placeholder": "Nom du produit"})
    description = StringField('description', validators=[ Length(min=10, max=20, message="La description doit contenir entre 2 et 20 caractères")], render_kw={"placeholder": "Description du produit"})
    price = StringField('price', validators=[  ], render_kw={"placeholder": "Prix du produit"})
    qte = StringField('qte', validators=[],render_kw={"placeholder": "Quantite du produit"})
    image = FileField('image', validators=[],render_kw={"placeholder": "Image du produit"})
    