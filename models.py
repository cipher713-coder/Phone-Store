# models.py
from ext import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    productbrand = db.Column(db.String, nullable=False)
    devicetype = db.Column(db.String, nullable=False)
    devicestorage = db.Column(db.String, nullable=False)
    modelname = db.Column(db.String, nullable=False)
    processor = db.Column(db.String, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    profile_image = db.Column(db.String, nullable=False)

class Signup(UserMixin, db.Model):
    __tablename__ = "registers"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String, unique=False)
    profile_picture = db.Column(db.String, unique=False)
    role = db.Column(db.String(10), default='user')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
