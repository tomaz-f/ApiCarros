from flask_restful import Resource
from flask import request
from flaskr.schema.carros_schemas import carros_schema, carro_schema
from flaskr.database.connection import db
from flaskr.models.carro_db_model import Carro


class CarrosResource(Resource):
    def get(self, id_car=None):
        if id_car:
            carro = Carro.query.get(id_car)
            return carro_schema.dump(carro)
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

    def put(self, id_car):
        json_data = request.get_json()
        if not json_data:
            return {'message': 'Nenhuma informação nova foi enviada'}, 400

        data = carro_schema.load(json_data)
        carro = Carro.query.get(id_car)
        carro.marca = data['marca']
        carro.nome = data['nome']
        carro.tipo = data['tipo']
        carro.ano = data['ano']
        carro.cor = data['cor']
        carro.preco = data['preco']

        db.session.commit()
        result = carro_schema.dump(carro)
        return {"status": 'sucesso', 'data': result}, 204

    def patch(self, id_car):
        carro = Carro.query.get(id_car)
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

    def delete(self, id_car):
        carro = Carro.query.get(id_car)
        db.session.delete(carro)
        db.session.commit()

        return {'message': 'Carro deletado'}, 204
