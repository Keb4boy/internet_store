from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy.orm import sessionmaker
from config import DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT, DB_USER
from internet_store.models import Vendor
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine

engine: AsyncEngine = create_async_engine(f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
async_session: AsyncSession = sessionmaker(engine, class_= AsyncSession)


app = FastAPI()


class VendorSchema(BaseModel):
    name: str

@app.get("/vendors/{vendor_id}", response_model=VendorSchema)
async def get_vendor(vendor_id: int):
    vendor = Vendor.query.get(vendor_id)
    return VendorSchema(id=vendor.id, name=vendor.name)

@app.post("/vendors/create")
async def add_vendor(item: VendorSchema):
    new_vendor = Vendor(**item)
    async with async_session() as session:
        session.add(new_vendor)
        await session.commit()
    return item

