from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .models import Base, HastaMetin, HastaSorular#, HastaGozlem

DATABASE_URL = "postgresql://testuser:test123@/ip-172-31-17-195/testdb"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Veritabanı tablolarını oluşturma fonksiyonu
def create_tables():
    Base.metadata.create_all(bind=engine)
