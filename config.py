from flask import Flask,session
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Security and database settings
app.config['SECRET_KEY'] = 'Booba123'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root@localhost:5433/flask_gestion"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
