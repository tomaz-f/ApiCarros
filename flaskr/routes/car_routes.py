from flask_restful import Api

from flaskr.resource.carros_resource import CarrosResource


def config_routes(app):
    api = Api()

    api.add_resource(CarrosResource, '/carros/', '/carros/<int:id_car>',
                     methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

    api.init_app(app)
