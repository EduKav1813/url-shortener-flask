from pathlib import Path


class Config:
    TESTING = False
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{Path(__file__).parent / 'instance/production.db'}"
    )


class TestConfig(Config):
    TESTING = True
    SQLALCHEMY_DATABASE_URI = (
        f"sqlite:///{Path(__file__).parent / 'instance/test.db'}"
    )
