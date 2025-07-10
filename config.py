# config.py
import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Flask
    SECRET_KEY = os.getenv("FLASK_SECRET_KEY", "chave_padrao_insegura")

    # Banco de Dados
    DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://postgres:F0xc0nn@10.8.2.213:5432/postgres")

    # Slack
    SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL", "")

    # Pastas
    UPLOAD_FOLDER = 'uploads'
    RESULT_FOLDER = 'static'
    HISTORICO_FILE = 'historico.json'
