from flask import Flask
from flask_restful import Api
from resource.carros_resource import CarrosResource
from utils.database import db


def config_database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mariadb+mariadbconnector://root:123456@localhost:3306/carros'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()


def config_routes(app):
    api = Api()

    api.add_resource(CarrosResource, '/carros/', '/carros/<int:id>', methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

    api.init_app(app)


def app_start():

    app = Flask(__name__)

    config_routes(app)
    config_database(app)

    return app


APP = app_start()

if __name__ == '__main__':
    APP.run(debug=True)
