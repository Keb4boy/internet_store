from internet_store.models import Vendor
from sqlalchemy.future import select
from internet_store.main import *
from internet_store.schemas.vendors import VendorSchema
    
# def post_vendors():
#     new_vendor = Vendor(**dict(item))
#     async with async_session() as session:
#         session.add(new_vendor)
#         await session.commit()
#     return item
    

async def get_vendor(vendor_id):
    async with async_session() as session:
        vendor = await session.execute(select(Vendor).where(Vendor.id == vendor_id))
    return vendor
    
