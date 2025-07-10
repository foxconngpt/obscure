from flask import Blueprint, render_template
from models import SessionLocal, Resultado

historico_bp = Blueprint("historico", __name__)

@historico_bp.route("/historico")
def historico():
    db = SessionLocal()
    registros = db.query(Resultado).order_by(Resultado.data_execucao.desc()).all()

    execucoes_por_data = {}
    for r in registros:
        data_str = r.data_execucao.strftime('%Y-%m-%d %H:%M:%S')
        if data_str not in execucoes_por_data:
            execucoes_por_data[data_str] = []
        execucoes_por_data[data_str].append({
            'ip': r.ip,
            'status': r.status,
            'interface': r.interface,
            'erro': r.erro,
            'descricao': r.descricao
        })

    execucoes = [{'data': data, 'resultados': resultados} for data, resultados in execucoes_por_data.items()]
    db.close()
    return render_template("historico.html", execucoes=execucoes)
