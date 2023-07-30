from internet_store.models import Order
from sqlalchemy.future import select
from internet_store.main import *
from internet_store.database import async_session, engine

async def get_order(order_id):
    async with engine.connect() as session:
        order = await session.execute(select(Order).where(Order.id == order_id))
        data = order.all()
        result = {}
        result.update(data)
    return result

async def post_order(item):
    new_order = Order(**dict(item))
    async with async_session() as session:
        session.add(new_order)
        await session.commit()
    return item
    