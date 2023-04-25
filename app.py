from flask import Flask
from flask_restful import Api
from app.resource.carros_resource import CarrosResource
from app.utils.database import config_database


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
