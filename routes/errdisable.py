from flask import Blueprint, render_template, request, redirect, flash, session, send_file
from netmiko import ConnectHandler
import pandas as pd
import io

errdisable_bp = Blueprint("errdisable", __name__)

# Dicionário de descrição de erros
REASON_DESCRIPTIONS = {
    "bpduguard": "BPDU Guard ativado: proteção contra loops na camada 2.",
    "psecure-violation": "Violação de segurança por MAC address não autorizado.",
    "link-flap": "Porta instável (subindo e caindo repetidamente).",
    "udld": "Link unidirecional detectado: falha em uma das direções.",
    "storm-control": "Tráfego excessivo de broadcast/multicast bloqueado.",
    "pagp-flap": "Mudança rápida no canal EtherChannel.",
    "dhcp-rate-limit": "Porta bloqueada por excesso de requisições DHCP.",
    "inline-power": "Erro ao fornecer energia PoE na porta.",
}

@errdisable_bp.route("/errdisable", methods=["GET", "POST"])
def diagnostico_errdisable():
    if request.method == "GET":
        return render_template("errdisable.html")

    resultados = []
    ips = request.form["ip"].replace(",", "").splitlines()
    username = request.form["username"]
    password = request.form["password"]

    session["ssh_username"] = username
    session["ssh_password"] = password

    for ip in ips:
        ip = ip.strip()
        if not ip:
            continue

        try:
            conn = ConnectHandler(
                device_type="cisco_ios",
                host=ip,
                username=username,
                password=password
            )
            conn.enable()
            output = conn.send_command("show interfaces status err-disabled")
            conn.disconnect()

            for line in output.splitlines():
                if "err-disabled" in line:
                    parts = line.split()
                    interface = parts[0]
                    reason = parts[-1]
                    resultados.append({
                        "ip": ip,
                        "interface": interface,
                        "status": "err-disabled",
                        "erro": reason,
                        "descricao": REASON_DESCRIPTIONS.get(reason, "Erro desconhecido."),
                        "reabilitada": False
                    })
        except Exception as e:
            resultados.append({
                "ip": ip,
                "interface": "N/A",
                "status": "falha",
                "erro": str(e),
                "descricao": "Erro de conexão ou comando",
                "reabilitada": False
            })

    session["diagnostico_resultados"] = [
        {
            "IP": r["ip"],
            "Interface": r["interface"],
            "Status": r["status"],
            "Erro": r["erro"],
            "Descrição": r["descricao"],
            "Reabilitada": "Sim" if r["reabilitada"] else "Não"
        }
        for r in resultados
    ]

    return render_template("resultado.html", resultados=resultados)

@errdisable_bp.route("/reabilitar", methods=["POST"])
def reabilitar_interface():
    ip = request.form["ip"]
    interface = request.form["interface"]

    username = session.get("ssh_username")
    password = session.get("ssh_password")

    if not username or not password:
        flash("⚠️ Usuário ou senha SSH não encontrados na sessão.", "danger")
        return redirect(request.referrer)

    try:
        conn = ConnectHandler(
            device_type="cisco_ios",
            host=ip,
            username=username,
            password=password
        )
        conn.enable()
        conn.send_config_set([
            f"interface {interface}",
            "shutdown",
            "no shutdown"
        ])
        conn.disconnect()
        flash(f"✅ Porta {interface} em {ip} reabilitada com sucesso.", "success")
    except Exception as e:
        flash(f"❌ Erro ao reabilitar {interface} em {ip}: {e}", "danger")

    return redirect(request.referrer)

@errdisable_bp.route("/download_excel", endpoint="download_excel")
def download_excel():
    data = session.get("diagnostico_resultados")

    if not data:
        flash("Nenhum resultado disponível para exportar.", "danger")
        return redirect("/errdisable")

    df = pd.DataFrame(data)
    output = io.BytesIO()
    with pd.ExcelWriter(output, engine='xlsxwriter') as writer:
        df.to_excel(writer, index=False, sheet_name='Erros')
    output.seek(0)

    return send_file(
        output,
        download_name="diagnostico_errdisable.xlsx",
        as_attachment=True,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )