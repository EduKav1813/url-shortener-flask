import logging
from pathlib import Path

from dal.db import db
from flask import Flask
from routes import index, redirect, register

DATABASE_PATH = f"sqlite:///{Path(__file__).parent / 'instance/test.db'}"


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_PATH
    logging.info(f"Setup database at: {DATABASE_PATH}")
    db.init_app(app)
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app()
    setup_database(app)

    app.register_blueprint(index.bp)
    app.register_blueprint(register.bp)
    app.register_blueprint(redirect.bp)

    app.run(debug=True)
