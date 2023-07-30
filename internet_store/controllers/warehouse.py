from internet_store.models import Warehouse
from sqlalchemy.future import select
from internet_store.main import *
from internet_store.database import async_session, engine


async def post_warehouse(item):
    new_warehouse = Warehouse(**dict(item))
    async with async_session() as session:
        session.add(new_warehouse)
        await session.commit()
    return item

    
async def get_warehouse(warehouse_id):
    async with engine.connect() as session:
        warehouse = await session.execute(select(Warehouse).where(Warehouse.id == warehouse_id))
        data = warehouse.all() 
        result = {}
        result.update(data)
    return result