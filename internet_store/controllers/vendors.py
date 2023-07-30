from internet_store.models import Vendor
from sqlalchemy.future import select
from internet_store.main import *
from internet_store.database import async_session, engine
from fastapi import HTTPException, Query


async def post_vendors(item):
    new_vendor = Vendor(**dict(item))
    async with async_session() as session:
        session.add(new_vendor)
        await session.commit()
    return item

    
async def get_vendor(vendor_id):
    async with engine.connect() as session:
        vendor = await session.execute(select(Vendor).where(Vendor.id == vendor_id))
        data = vendor.all() 
        result = {}
        result.update(data)
    return result

async def get_all_vendor(offset: int, limit: int):
    async with engine.connect() as session:
        vendor = await session.execute(select(Vendor).offset(offset).limit(limit))
        data = vendor.all() 
        result = {}
        result.update(data)
    return result