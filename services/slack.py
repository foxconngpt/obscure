import requests
from flask import has_request_context, session

def enviar_slack(resultados, webhook_url):
    if has_request_context() and not session.get('slack_ativo', True):
        return
    total = len(resultados)
    erros = [r for r in resultados if r.get('erro')]
    texto = f"*Diagnóstico Concluído*\nTotal de IPs analisados: {total}\nErros encontrados: {len(erros)}"
    detalhes = "\n".join([f"{r['ip']} - {r['interface']} - {r['erro']}" for r in erros[:10]])
    if detalhes:
        texto += f"\n\n*Erros Detalhados:*\n{detalhes}"
    else:
        texto += "\n✅ Nenhum erro encontrado."
    payload = {"text": texto}
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except Exception as e:
        print(f"Erro ao enviar para Slack: {e}")
