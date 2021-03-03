from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    role = db.Column(db.String(35), unique=True, nullable=False),
    firstname = db.Column(db.String(25), nullable=False),
    lastname = db.Column(db.String(25), nullable=False),
    email = db.Column(db.String(35), nullable=False),
    phone = db.Column(db.String(35), nullable=True)


class Form(db.Model):
    id = db.Column(db.Integer, primary_key=True),
    name = db.Column(db.String(15), unique=True, nullable=False),
    sitepath = db.Column(db.String(21), unique=True, nullable=False)