from pathlib import Path

from flask import Flask

from dal.db import db
from routes import index, register


def create_app():
    app = Flask(__name__)
    app.config["DEBUG"] = True
    app.config[
        "SQLALCHEMY_DATABASE_URI"
    ] = f"sqlite:///{Path(__file__).parent / 'test.db'}"
    db.init_app(app)
    return app


def setup_database(app):
    with app.app_context():
        db.create_all()


if __name__ == "__main__":
    app = create_app()
    setup_database(app)

    app.register_blueprint(index.bp)
    app.register_blueprint(register.bp)

    app.run(debug=True)
