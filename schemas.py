from pydantic import BaseModel
from typing import List
from datetime import datetime

# USER
class UserCreate(BaseModel):
    email: str
    password: str
    role: str = "user"

class UserResponse(BaseModel):
    id: int
    email: str
    role: str
    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

# TRANSAKSI 
class TransaksiBase(BaseModel):
    petani_id: int
    berat_tonase: float
    kualitas: str

class TransaksiCreate(TransaksiBase):
    pass

class TransaksiResponse(TransaksiBase):
    id: int
    tanggal_masuk: datetime
    class Config:
        from_attributes = True

# PETANI 
class PetaniBase(BaseModel):
    nama: str
    lokasi_kebun: str
    kontak: str

class PetaniCreate(PetaniBase):
    pass

class PetaniResponse(PetaniBase):
    id: int
    transaksi: List[TransaksiResponse] = [] 
    class Config:
        from_attributes = True