from netmiko import ConnectHandler

def executar_diagnostico(ip_list, ssh_user, ssh_pass, progresso_callback=None):
    resultados = []

    for i, ip in enumerate(ip_list, 1):
        if progresso_callback and progresso_callback("cancelado"):
            progresso_callback(f"\n❌ Execução cancelada.")
            break

        if progresso_callback:
            progresso_callback(f"\nVerificando: {ip}")

        try:
            device = {
                'device_type': 'cisco_ios',
                'host': ip,
                'username': ssh_user,
                'password': ssh_pass,
                'timeout': 10
            }
            con = ConnectHandler(**device)
            output = con.send_command("show interfaces status err-disabled")

            if not output.strip():
                if progresso_callback:
                    progresso_callback(" ✅ Sem erros.")
                con.disconnect()
                continue

            for linha in output.splitlines():
                if linha.lower().startswith("port") or not linha.strip():
                    continue
                cols = linha.split()
                if len(cols) >= 2:
                    interface = cols[0]
                    reason = cols[-1].lower()
                    descricao = {
                        "psecure-violation": "MAC Address não autorizado",
                        "bpduguard": "Loop detectado - BPDU",
                        "link-flap": "Oscilação de link",
                        "storm-control": "Tempestade de broadcast",
                        "udld": "Unidirecionalidade detectada",
                        "channel-misconfig": "Erro de EtherChannel",
                        "pagp-flap": "PAgP com flap",
                        "pagp-unsupported": "PAgP não suportado",
                        "twinax-rate-unsupported": "Incompatibilidade com cabo Twinax",
                    }.get(reason, "Motivo desconhecido")

                    resultados.append({
                        'ip': ip,
                        'status': 'Conectado',
                        'interface': interface,
                        'erro': reason,
                        'descricao': descricao
                    })

            con.disconnect()
            if progresso_callback:
                progresso_callback(" ✅ Processado.")

        except Exception as e:
            if progresso_callback:
                progresso_callback(f" ❌ Erro: {e}")

    return resultados
