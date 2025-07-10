# init_db.py
from sqlalchemy import create_engine
from models import Base, DATABASE_URL

def inicializar_banco():
    print("🔄 Conectando ao banco...")
    engine = create_engine(DATABASE_URL)
    
    print("📦 Criando tabelas (se não existirem)...")
    Base.metadata.create_all(bind=engine)
    
    print("✅ Banco de dados pronto!")

if __name__ == "__main__":
    inicializar_banco()
