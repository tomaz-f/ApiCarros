from utils.database import db


class Carro(db.Model):
    __tablename__ = "Carros"

    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(255))
    nome = db.Column(db.String(255))
    ano = db.Column(db.Integer)
    cor = db.Column(db.String(255))
    tipo = db.Column(db.String(255))
