from internet_store.models import Buyer
from sqlalchemy.future import select
from internet_store.main import *
from internet_store.database import async_session, engine


async def get_buyer(buyer_id):
    async with engine.connect() as session:
        buyer = await session.execute(select(Buyer).where(Buyer.id == buyer_id))
        data = buyer.all() 
        result = {}
        result.update(data)
    return result



async def post_buyer(item):
        new_buyer = Buyer(**dict(item))
        async with async_session() as session:
            session.add(new_buyer)
            await session.commit()
        return item