from flask import Flask
from flask_restful import Api

from resource.carros_resource import ListaCarros, ModificaCarro
from utils.database import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:123456@localhost:3306/carros'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
with app.app_context():
    db.create_all()
api = Api(app)


api.add_resource(ListaCarros, '/carros')
api.add_resource(ModificaCarro, '/carros/<int:id_carro>')

if __name__ == '__main__':
    app.run(debug=True)
