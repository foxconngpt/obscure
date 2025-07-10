from flask import Blueprint, render_template
from models import Resultado, SessionLocal

analise_bp = Blueprint('analise', __name__)

@analise_bp.route('/analise')
def analise():
    db = SessionLocal()
    resultados = db.query(Resultado).all()
    db.close()

    erros_por_tipo = {}
    erros_por_ip = {}

    for r in resultados:
        if r.erro:
            erros_por_tipo[r.erro] = erros_por_tipo.get(r.erro, 0) + 1
            erros_por_ip[r.ip] = erros_por_ip.get(r.ip, 0) + 1

    return render_template('analise.html', erros_por_tipo=erros_por_tipo, erros_por_ip=erros_por_ip)
