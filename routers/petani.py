from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schemas, database
from routers.auth import get_current_user

router = APIRouter()

# Fungsi proteksi khusus Admin
def require_admin(current_user: models.User = Depends(get_current_user)):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Akses ditolak: Hanya untuk Admin")
    return current_user

@router.post("/", response_model=schemas.PetaniResponse)
def tambah_petani(petani: schemas.PetaniCreate, db: Session = Depends(database.get_db), current_user: models.User = Depends(require_admin)):
    db_petani = models.Petani(**petani.dict())
    db.add(db_petani)
    db.commit()
    db.refresh(db_petani)
    return db_petani

@router.get("/", response_model=list[schemas.PetaniResponse])
def lihat_semua_petani(db: Session = Depends(database.get_db), current_user: models.User = Depends(get_current_user)):
    return db.query(models.Petani).all()