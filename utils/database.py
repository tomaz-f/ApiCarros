from flask_sqlalchemy import SQLAlchemy
from decouple import config as configdecouple

db = SQLAlchemy()


def config_database(app):

    app.config['SQLALCHEMY_DATABASE_URI'] = configdecouple('DB_URL')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    with app.app_context():
        db.create_all()
