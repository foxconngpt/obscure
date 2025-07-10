from flask import Blueprint

common_bp = Blueprint("common", __name__)

@common_bp.route("/ping")
def ping():
    return "pong"
