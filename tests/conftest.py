import pytest

from backend.app import create_app, db, register_blueprits
from backend.config import TestConfig


@pytest.fixture
def app():
    app = create_app(TestConfig)
    register_blueprits(app)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def runner(app):
    return app.test_cli_runner()
