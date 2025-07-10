
from netmiko import ConnectHandler, NetMikoAuthenticationException, NetMikoTimeoutException
import time

def executar_diagnostico(ip_list, username, password, socketio):
    for ip in ip_list:
        socketio.emit('log_update', f"🔌 Conectando ao switch {ip}...")
        try:
            device = {
                'device_type': 'cisco_ios',
                'host': ip,
                'username': username,
                'password': password,
            }
            net_connect = ConnectHandler(**device)
            output = net_connect.send_command("show interface status err-disabled")
            socketio.emit('log_update', f"📥 Resultado {ip}: conexão estabelecida.")
            net_connect.disconnect()
        except NetMikoAuthenticationException:
            socketio.emit('log_update', f"❌ Falha de autenticação em {ip}\n")
        except NetMikoTimeoutException:
            socketio.emit('log_update', f"⏱️ Timeout ao conectar em {ip}\n")
        except Exception as e:
            socketio.emit('log_update', f"⚠️ Erro desconhecido em {ip}: {str(e)}\n")
        time.sleep(1)
