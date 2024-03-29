from marshmallow import Schema, fields


class CarroSchema(Schema):
    id_car = fields.Int()
    marca = fields.Str(required=True)
    nome = fields.Str(required=True)
    ano = fields.Int(required=True)
    cor = fields.Str(required=True)
    tipo = fields.Str(required=True)
    preco = fields.Float(required=True)


carro_schema = CarroSchema()
carros_schema = CarroSchema(many=True)
