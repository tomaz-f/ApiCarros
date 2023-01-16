from flask_restful import Resource
from flask import request
from schema.carros_schemas import carros_schema, carro_schema
from utils.database import db
from model.carro_db_model import Carro


class CarrosResource(Resource):
    def get(self, id=None):
        if id is not None:
            carro = Carro.query.get(id)
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

    def put(self, id):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'Nenhuma informação nova foi enviada'}, 400

        data = carro_schema.load(json_data)
        carro = Carro.query.get(id)
        carro.marca = data['marca']
        carro.nome = data['nome']
        carro.tipo = data['tipo']
        carro.ano = data['ano']
        carro.cor = data['cor']

        db.session.commit()
        result = carro_schema.dump(carro)
        return {"status": 'sucesso', 'data': result}, 204

    def patch(self, id):
        carro = Carro.query.get(id)
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

    def delete(self, id):
        carro = Carro.query.get(id)
        db.session.delete(carro)
        db.session.commit()

        return {'message': 'Carro deletado'}
