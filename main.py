from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api, Resource

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)
ma = Marshmallow(app)
api = Api(app)


class Carro(db.Model):
    __tablename__ = "Carros"

    id = db.Column(db.Integer, primary_key=True)
    marca = db.Column(db.String(255))
    nome = db.Column(db.String(255))
    ano = db.Column(db.Integer)
    cor = db.Column(db.String(255))
    tipo = db.Column(db.String(255))

    def __repr__(self):
        return '<Carro %s' % self.marca


with app.app_context():
    db.create_all()
    db.session.commit()


class CarroSchema(ma.Schema):
    class Meta:
        fields = ("id", "marca", "nome", "ano", "cor", "tipo")
        model = Carro


carro_schema = CarroSchema()
carros_schema = CarroSchema(many=True)


class ListaCarros(Resource):
    def get(self):
        carros = Carro.query.all()
        return carros_schema.dump(carros)

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
        return carro_schema.dump(novo_carro)


class PostResource(Resource):
    def get(self, id_carro):
        carro = Carro.query.get_or_404(id_carro)
        return carro_schema.dump(carro)

    def update(self, id_carro):
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
        return carro_schema.dump()

    def delete(self, id_carro):
        carro = Carro.query.get_or_404(id_carro)

        db.session.delete(carro)
        db.session.commit()
        return '', 204


api.add_resource(ListaCarros, '/carros')
api.add_resource(PostResource, '/carros/<int:id_carro>')

if __name__ == '__main__':
    app.run(debug=True)
