from internet_store.models import Orders_product
from sqlalchemy.future import select
from internet_store.main import *
from internet_store.database import async_session, engine

async def get_orders_product(orders_product_id):
    async with engine.connect() as session:
        orders_product = await session.execute(select(Orders_product).where(Orders_product.id == orders_product_id))
        data = orders_product.all()
        result = {}
        result.update(data)
    return result

async def post_orders_product(item):
    new_orders_roduct = Orders_product(**dict(item))
    async with async_session() as session:
        session.add(new_orders_roduct)
        await session.commit()
    return item