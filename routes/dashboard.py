from flask import Blueprint, render_template, request, redirect, url_for, session
import os

dashboard_bp = Blueprint('dashboard', __name__)

# Redireciona a rota raiz para o dashboard
@dashboard_bp.route('/')
def index():
    return redirect(url_for('dashboard.dashboard'))

# Página principal do dashboard
@dashboard_bp.route('/dashboard')
def dashboard():
    lista_ips = []
    nome_arquivo = None
    slack_ativo = session.get('slack_ativo', True)

    if os.path.exists('ips_path.txt'):
        try:
            with open('ips_path.txt') as path_file:
                caminho = path_file.read().strip()
                with open(caminho) as f:
                    lista_ips = [l.strip() for l in f if l.strip()]
                nome_arquivo = os.path.basename(caminho)
        except Exception:
            pass

    return render_template('dashboard.html', lista_ips=lista_ips, arquivo_atual=nome_arquivo, slack_ativo=slack_ativo)

# Alterna a ativação de notificação via Slack
@dashboard_bp.route('/alternar_notificacao', methods=['POST'])
def alternar_notificacao():
    atual = session.get('slack_ativo', True)
    session['slack_ativo'] = not atual
    return redirect(url_for('dashboard.dashboard'))
