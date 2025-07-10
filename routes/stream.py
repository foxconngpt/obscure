from flask import Blueprint, Response
import time

stream_bp = Blueprint('stream', __name__)

def generate_logs():
    ips = ["10.8.35.104", "10.8.35.105", "10.8.35.106", "10.8.35.107", "10.8.35.108"]
    for ip in ips:
        yield f"data: Conectando ao switch {ip}...\n\n"
        time.sleep(1)
        yield f"data: SSH OK. Executando comandos no {ip}...\n\n"
        time.sleep(1)
        yield f"data: Comando executado com sucesso no {ip}!\n\n"
        time.sleep(0.5)
    yield "data: Fim da execução.\n\n"

@stream_bp.route('/stream_logs')
def stream_logs():
    return Response(generate_logs(), mimetype='text/event-stream')