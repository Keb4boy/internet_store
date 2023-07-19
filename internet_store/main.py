from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlalchemy import VARCHAR, create_engine
from sqlalchemy.orm import Session, sessionmaker
from config import DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT, DB_USER
from internet_store.models import Vendor


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=create_engine(f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'))

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class VendorResponse(BaseModel):
    id: int
    name: VARCHAR(255)

@app.get("/vendors/{vendor_id}", response_model=VendorResponse)
def get_vendor(vendor_id: int):
    vendor = Vendor.query.get(vendor_id)
    return VendorResponse(id=vendor.id, name=vendor.name)

@app.post("/vendors", response_model=VendorResponse)
def add_vendor(new_vendor: Vendor):
    db = SessionLocal()
    db.add(new_vendor)
    db.commit()
    db.refresh(new_vendor)
    return new_vendor

