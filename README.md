# 🔍 Diagnóstico de Switches Cisco

Sistema web em Flask para realizar diagnóstico automático em switches Cisco via SSH, identificando interfaces com erro (`err-disabled`), analisando causas, e gerando relatórios com gráficos e exportação em Excel.

---

## 🚀 Funcionalidades

- Upload de lista de IPs para varredura
- Execução automatizada via Netmiko
- Detecção de causas `err-disabled` (como `bpduguard`, `storm-control`, etc.)
- Análise gráfica com Chart.js
- Histórico persistente no banco PostgreSQL
- Reabilitação de portas erradas via interface
- Exportação para Excel
- Notificação no Slack
- Interface Web com Flask + Jinja2

---

## 📦 Estrutura do Projeto

```
diagnostico_app/
├── app.py                  # Ponto de entrada Flask
├── config.py               # Configuração (usa .env)
├── models.py               # Tabela Resultado (SQLAlchemy)
│
├── routes/                 # Blueprints por funcionalidade
│   ├── dashboard.py
│   ├── diagnostico.py
│   ├── historico.py
│   ├── analise.py
│   └── common.py
│
├── services/               # Lógica de negócio desacoplada
│   ├── executor.py         # Execução SSH e diagnóstico
│   └── slack.py            # Envio de alerta para Slack
│
├── templates/              # HTMLs (Jinja2)
├── static/                 # Arquivos CSS/JS
├── uploads/                # Arquivos de IPs enviados
│
├── .env                    # Variáveis de ambiente
├── requirements.txt        # Dependências Python
├── README.md               # Este arquivo
```

---

## ⚙️ Instalação

### Pré-requisitos

- Python 3.10+
- PostgreSQL 12+
- Virtualenv (recomendado)

### 1. Clone o projeto e instale o ambiente

```bash
git clone https://github.com/seu-usuario/diagnostico-app.git
cd diagnostico-app
python -m venv .venv
.\.venv\Scriptsctivate  # Windows
pip install -r requirements.txt
```

### 2. Configure o `.env`

Crie um arquivo `.env` na raiz com:

```env
FLASK_SECRET_KEY=sua_chave_secreta
DATABASE_URL=postgresql://postgres:senha@localhost:5432/diagnostico
SLACK_WEBHOOK_URL=https://hooks.slack.com/services/SEU/WEBHOOK
```

### 3. Inicialize o banco

```bash
python models.py
```

ou crie um `init_db.py` para `Base.metadata.create_all()`.

---

## ▶️ Executando

```bash
python app.py
```

Acesse: [http://localhost:5000](http://localhost:5000)

---

## 📊 Tecnologias usadas

- **Flask** – Web framework
- **SQLAlchemy** – ORM
- **PostgreSQL** – Banco de dados relacional
- **Netmiko** – SSH para switches Cisco
- **Openpyxl** – Geração de planilhas Excel
- **Chart.js** – Gráficos dinâmicos
- **Slack Webhook** – Notificações integradas

---

## 📌 Próximas melhorias sugeridas

- ✅ Login/autenticação de usuários
- ✅ Dashboard com filtros por IP/data/erro
- ✅ Logs de execução em arquivo
- ✅ Deploy com Gunicorn + Nginx (produção)
- ✅ Testes unitários (PyTest)

---

## 🙌 Contribuição

1. Faça um fork
2. Crie uma branch `feature/minha-funcionalidade`
3. Commit suas mudanças
4. Envie um pull request

---

## 🛡️ Licença

Este projeto é licenciado sob os termos da MIT License.