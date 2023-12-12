from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Base, HastaMetin, HastaSorular#, HastaGozlem

DATABASE_URL = "postgresql:5432//postgres:123@localhost:5432/postgres"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanı tablolarını oluşturma fonksiyonu
def create_tables():
    Base.metadata.create_all(bind=engine)
