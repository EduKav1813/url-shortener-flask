import logging

from app import create_app, register_blueprits
from config import Config

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    app = create_app(Config)
    register_blueprits(app)

    app.run(debug=True)
