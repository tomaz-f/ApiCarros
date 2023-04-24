from flask_restful import Resource
from flask import request
from schema.carros_schemas import carros_schema, carro_schema
from utils.database import db
from models.carro_db_model import Carro


class CarrosResource(Resource):
    def get(self, identifier=None):
        if identifier is not None:
            carro = Carro.query.get(identifier)
            return carro_schema.dump(carro)
        else:
            carros = Carro.query.all()
            return carros_schema.dump(carros)

    def post(self):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'Nenhuma informação foi enviada'}, 400

        data = carro_schema.load(json_data)
        carro = Carro(**data)

        db.session.add(carro)
        db.session.commit()
        result = carro_schema.dump(carro)

        return {"status": 'sucesso', 'data': result}, 201

    def put(self, identifier):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'Nenhuma informação nova foi enviada'}, 400

        data = carro_schema.load(json_data)
        carro = Carro.query.get(identifier)
        carro.marca = data['marca']
        carro.nome = data['nome']
        carro.tipo = data['tipo']
        carro.ano = data['ano']
        carro.cor = data['cor']

        db.session.commit()
        result = carro_schema.dump(carro)
        return {"status": 'sucesso', 'data': result}, 204

    def patch(self, identifier):
        carro = Carro.query.get(identifier)
        if not carro:
            return {'message': 'Carro não encontrado'}, 404

        json_data = request.get_json()
        if not json_data:
            return {'message': 'Nenhuma informação nova foi enviada'}, 400

        data = carro_schema.load(json_data, partial=True)
        for key, value in data.items():
            setattr(carro, key, value)

        db.session.commit()
        result = carro_schema.dump(carro)

        return {"status": 'sucesso', 'data': result}, 204

    def delete(self, identifier):
        carro = Carro.query.get(identifier)
        db.session.delete(carro)
        db.session.commit()

        return {'message': 'Carro deletado'}, 204
