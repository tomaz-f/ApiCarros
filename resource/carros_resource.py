from flask_restful import Resource
from flask import request

from model.carros_schemas import CarroSchema
from utils.database import db
from model.carro_db_model import Carro


class ListaCarros(Resource):

    def get(self, carro_id=None):
        if carro_id is not None:
            carro = Carro.query.get(carro_id)
            if carro:
                carro_schema = CarroSchema()
                return carro_schema.dump(carro)
            else:
                return {'error': 'Carro não encontrado'}, 404
        else:
            carros = Carro.query.all()
            carro_schema = CarroSchema(many=True)
            return carro_schema.dump(carros)

    def post(self):
        novo_carro = Carro(
            marca=request.json['marca'],
            nome=request.json['nome'],
            ano=request.json['ano'],
            cor=request.json['cor'],
            tipo=request.json['tipo']
        )
        db.session.add(novo_carro)
        db.session.commit()
        return schema.dump(novo_carro)


class ModificaCarro(Resource):

    def get(self, id_carro):
        carro = Carro.query.get_or_404(id_carro)
        return schema.dump(carro)

    def put(self, id_carro):
        carro = Carro.query.get_or_404(id_carro)

        if 'marca' in request.json:
            carro.marca = request.json['marca']
        if 'nome' in request.json:
            carro.nome = request.json['nome']
        if 'ano' in request.json:
            carro.ano = request.json['ano']
        if 'cor' in request.json:
            carro.cor = request.json['cor']
        if 'tipo' in request.json:
            carro.tipo = request.json['tipo']

        db.session.commit()
        return schema.dump(carro)

    def delete(self, id_carro):
        carro = Carro.query.get_or_404(id_carro)

        db.session.delete(carro)
        db.session.commit()
        return '', 204
