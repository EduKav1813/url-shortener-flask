from dal.db import get_url_by_code
from flask import Blueprint, redirect

bp = Blueprint("redirect", __name__, url_prefix="/redirect")


@bp.route("/<code>", methods=["GET"])
def redirect_to_url(code):
    if code:
        target_url = get_url_by_code(code)
        return redirect(target_url)
    else:
        return "Please provide shortened code"
