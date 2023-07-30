from internet_store.models import Warehouse_product
from sqlalchemy.future import select
from internet_store.main import *
from internet_store.database import async_session, engine

async def get_warehouse_product(warehouse_product_id):
    async with engine.connect() as session:
        warehouse_product = await session.execute(select(Warehouse_product).where(Warehouse_product.id == warehouse_product_id))
        data = warehouse_product.all()
        result = {}
        result.update(data)
    return result

async def post_warehouse_product(item):
    new_product = Warehouse_product(**dict(item))
    async with async_session() as session:
        session.add(new_product)
        await session.commit()
    return item