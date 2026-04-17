from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
import models
from database import engine, get_db
from routers import auth, petani, transaksi

models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Sistem Timbangan Sawit API - UTS Haris")

# Menghubungkan router
app.include_router(auth.router, prefix="/auth", tags=["Autentikasi"])
app.include_router(petani.router, prefix="/petani", tags=["Manajemen Petani"])
app.include_router(transaksi.router, prefix="/transaksi", tags=["Catatan Timbangan"])

@app.get("/", tags=["Root"])
def root():
    return {"message": "Sistem Informasi Timbangan Sawit Haris Berhasil Dijalankan"}

@app.get("/dashboard", tags=["Dashboard"])
def get_dashboard_summary(db: Session = Depends(get_db)):
    # 1. Hitung total petani yang terdaftar
    total_petani = db.query(func.count(models.Petani.id)).scalar()
    
    # 2. Hitung total berat tonase dari seluruh transaksi
    total_tonase = db.query(func.sum(models.Transaksi.berat_tonase)).scalar() or 0
    
    # 3. Hitung rata-rata berat timbangan per transaksi
    rata_rata_berat = db.query(func.avg(models.Transaksi.berat_tonase)).scalar() or 0
    
    # 4. Ambil 3 aktivitas transaksi terbaru
    recent_activity = db.query(models.Transaksi).order_by(models.Transaksi.id.desc()).limit(3).all()

    return {
        "status": "success",
        "data": {
            "summary": {
                "total_petani": total_petani,
                "total_tonase_masuk": f"{total_tonase:.2f} Ton",
                "rata_rata_timbangan": f"{rata_rata_berat:.2f} Ton"
            },
            "recent_activity": recent_activity
        }
    }