from flask_restful import Api

from app.resource.carros_resource import CarrosResource

def config_routes(app):
    api = Api()

    api.add_resource(CarrosResource, '/carros/', '/carros/<int:id>',
                     methods=['GET', 'POST', 'PUT', 'PATCH', 'DELETE'])

    api.init_app(app)
