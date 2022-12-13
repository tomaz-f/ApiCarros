from flask import Flask
from flask_restful import Api
from resource.carros_resource import ListaCarros, ModificaCarro
from utils.database import db


def config_routes(app):
    api = Api()

    api.add_resource(ListaCarros, '/carros')
    api.add_resource(ModificaCarro, '/carros/<int:id_carro>')

    api.init_app(app)


def app_start():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:123456@localhost:3306/carros'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()

    config_routes(app)
    return app


APP = app_start()

if __name__ == '__main__':
    APP.run(debug=True)
