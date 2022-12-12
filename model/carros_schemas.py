from marshmallow import Schema
from model.carro_db_model import Carro


class CarroSchema(Schema):
    class Meta:
        fields = ("id", "marca", "nome", "ano", "cor", "tipo")
        model = Carro


carro_schema = CarroSchema()
carros_schema = CarroSchema(many=True)
