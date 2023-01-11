from utils.database import db


class Carro(db.Model):
    __tablename__ = "Carros"

    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(255))
    nome = db.Column(db.String(255))
    ano = db.Column(db.Integer)
    cor = db.Column(db.String(255))
    tipo = db.Column(db.String(255))

    def __init__(self, marca, nome, ano, cor, tipo):
        self.marca = marca
        self.nome = nome
        self.ano = ano
        self.cor = cor
        self.tipo = tipo
