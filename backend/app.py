import logging
import os

from dal.db import db
from flask import Flask
from routes import redirect, register


def delete_database(database_path):
    if os.path.exists(database_path):
        os.remove(database_path)


def register_blueprits(app):
    app.register_blueprint(register.bp)
    app.register_blueprint(redirect.bp)


def create_app(config):
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
    logging.info(f"Setup database at: {config.SQLALCHEMY_DATABASE_URI}")
    db.init_app(app)
    with app.app_context():
        db.create_all()
    return app
