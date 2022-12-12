from marshmallow import Schema, fields


class CarroSchema(Schema):
    marca = fields.Str(required=True)
    nome = fields.Str(required=True)
    ano = fields.Int(required=True)
    cor = fields.Str(required=True)
    tipo = fields.Str(required=True)


schema = CarroSchema()
carros_schema = CarroSchema(many=True)