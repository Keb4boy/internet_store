from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker
from config import DB_PASSWORD, DB_HOST, DB_NAME, DB_PORT, DB_USER
from internet_store.models import Vendor, Buyer
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from internet_store.routers.vendors import router
from fastapi import APIRouter

engine: AsyncEngine = create_async_engine(f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}')
async_session: AsyncSession = sessionmaker(engine, class_= AsyncSession)


app = FastAPI()

app.include_router(router)


# class VendorSchema(BaseModel):
#     name: str


# @app.get("/vendors/{vendor_id}", response_model=VendorSchema)
# async def get_vendor(vendor_id: int):
#     async with async_session() as session:
#         ven = await session.execute(select(Vendor).where(Vendor.id == vendor_id))
#         vendor = ven.scalar_one_or_none()
#         return vendor


# @app.post("/vendors/create")
# async def add_vendor(item: VendorSchema):
#     new_vendor = Vendor(**dict(item))
#     async with async_session() as session:
#         session.add(new_vendor)
#         await session.commit()
#     return item

class BuyerSchema(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str
    login: str

@app.get('/buyer/{buyer_id}')
async def get_buyer(buyer_id: int):
    async with async_session() as session:
        buy = await session.execute(select(Buyer).where(Buyer.id == buyer_id))
        buyer = buy.scalar_one_or_none()
        return buyer
    
@app.get('/buyers')
async def get_buyer():
    async with async_session() as session:
        buy = await session.execute(select(Buyer))
        return buy

@app.post("/buyer/create")
async def add_buyer(item: BuyerSchema):
    new_buyer = Buyer(**dict(item))
    async with async_session() as session:
        session.add(new_buyer)
        await session.commit()
    return item

class OrdersSchema(BaseModel):
    id: int
    buyer_id: int

# @app.get("/orders/{order_id}")
# async def get_order():
