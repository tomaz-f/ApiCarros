from marshmallow import Schema
from marshmallow.fields import Int, Str


class CarroSchema(Schema):
    marca = Str(required=True)
    nome = Str(required=True)
    ano = Int(required=True)
    cor = Str(required=True)
    tipo = Str(required=True)


schema = CarroSchema()
carros_schema = CarroSchema(many=True)
