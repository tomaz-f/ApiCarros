import os
from flask import Flask
from flaskr.database.connection import config_database
from flaskr.routes.car_routes import config_routes


def create_app():

    app = Flask(__name__, instance_relative_config=True)

    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    config_routes(app)
    config_database(app)

    return app


APP = create_app()

if __name__ == '__main__':
    APP.run(debug=True)
