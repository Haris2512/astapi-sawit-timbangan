from sqlalchemy import Column, Integer, String, Float, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from database import Base
import datetime

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")

class Petani(Base):
    __tablename__ = "petani"
    id = Column(Integer, primary_key=True, index=True)
    nama = Column(String, index=True)
    lokasi_kebun = Column(String)
    kontak = Column(String)

    transaksi = relationship("Transaksi", back_populates="pemilik", cascade="all, delete-orphan")

class Transaksi(Base):
    __tablename__ = "transaksi_timbangan"
    id = Column(Integer, primary_key=True, index=True)
    petani_id = Column(Integer, ForeignKey("petani.id"))
    berat_tonase = Column(Float)
    kualitas = Column(String)
    tanggal_masuk = Column(DateTime, default=datetime.datetime.utcnow)

    pemilik = relationship("Petani", back_populates="transaksi")