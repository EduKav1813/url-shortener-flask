from dal.db import create_url
from flask import Blueprint, jsonify, request

bp = Blueprint("register", __name__, url_prefix="/register")


@bp.route("/", methods=["POST"])
def register_url():
    url = request.args.get("url")
    if url:
        new_url = create_url(url)
        return jsonify({"url": new_url.original_url, "code": new_url.code})
    else:
        return "Please provide URL"
