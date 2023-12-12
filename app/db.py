from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Base, HastaMetin, HastaSorular#, HastaGozlem

DATABASE_URL = "postgres://localhost:J1WDQBgrkC89NUC80FxiMX6fxsnTJ9Zn@dpg-clse4m63d79c739gn2pg-a/postgres_db_jlut"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanı tablolarını oluşturma fonksiyonu
def create_tables():
    Base.metadata.create_all(bind=engine)
