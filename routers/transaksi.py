from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from routers.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=schemas.TransaksiResponse)
def buat_catatan_timbangan(transaksi: schemas.TransaksiCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    # Cek apakah ID Petani valid
    petani = db.query(models.Petani).filter(models.Petani.id == transaksi.petani_id).first()
    if not petani:
        raise HTTPException(status_code=404, detail="ID Petani tidak ditemukan")
    
    data_baru = models.Transaksi(**transaksi.dict())
    db.add(data_baru)
    db.commit()
    db.refresh(data_baru)
    return data_baru

@router.get("/", response_model=list[schemas.TransaksiResponse])
def lihat_semua_timbangan(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Transaksi).all()