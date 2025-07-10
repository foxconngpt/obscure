from models import Base
from config import Config
from sqlalchemy import create_engine

engine = create_engine(Config.DATABASE_URL)
Base.metadata.create_all(bind=engine)
print("✅ Banco de dados inicializado com sucesso.")