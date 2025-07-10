# init_db.py
"""Script para inicializar o banco de dados."""

from sqlalchemy import create_engine

from config import Config
from models import Base

def inicializar_banco():
    print("🔄 Conectando ao banco...")
    engine = create_engine(Config.DATABASE_URL)
    
    print("📦 Criando tabelas (se não existirem)...")
    Base.metadata.create_all(bind=engine)
    
    print("✅ Banco de dados pronto!")

if __name__ == "__main__":
    inicializar_banco()
