from sqlalchemy import Column, Integer, String, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from config import Config

engine = create_engine(Config.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Resultado(Base):
    __tablename__ = "resultados"
    id = Column(Integer, primary_key=True, index=True)
    ip = Column(String, index=True)
    status = Column(String)
    interface = Column(String)
    erro = Column(String)
    descricao = Column(String)
    data_execucao = Column(DateTime, default=datetime.utcnow)

# Criar as tabelas
Base.metadata.create_all(bind=engine)
