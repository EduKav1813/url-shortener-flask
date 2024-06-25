import random

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Url(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(255), unique=False, nullable=False)
    code = db.Column(db.String(10), unique=True, nullable=False)


def _generate_code() -> str:
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return "".join(random.choice(chars) for _ in range(10))


def create_url(url: str):
    new_url = Url(original_url=url, code=_generate_code())
    db.session.add(new_url)
    db.session.commit()
    return new_url


def get_all_urls():
    return Url.query.all()
