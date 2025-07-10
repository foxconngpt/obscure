
from flask import Blueprint, render_template, request, redirect, url_for
from flask_socketio import emit
from threading import Thread
from services.diagnostico_service import executar_diagnostico

diagnostico_bp = Blueprint('diagnostico', __name__)

socketio_ref = None

@diagnostico_bp.route("/diagnostico")
def diagnostico():
    return render_template("diagnostico.html")

@diagnostico_bp.route("/executar_diagnostico", methods=["POST"])
def executar():
    global socketio_ref
    ips = request.form.get("ips", "")
    username = request.form.get("username", "")
    password = request.form.get("password", "")

    ip_list = [ip.strip() for ip in ips.splitlines() if ip.strip()]
    if ip_list and socketio_ref:
        thread = Thread(target=executar_diagnostico, args=(ip_list, username, password, socketio_ref))
        thread.start()
    return redirect(url_for("diagnostico.diagnostico"))
