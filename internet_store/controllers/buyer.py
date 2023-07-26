from pydantic import BaseModel
from internet_store.models import Vendor
from sqlalchemy.future import select
from internet_store.main import *

class BuyerSchema(BaseModel):
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str
    login: str
    
def get_buyer(buyer_id):
    async def get_buyer(buyer_id: int):
        async with async_session() as session:
            buy = await session.execute(select(Buyer).where(Buyer.id == buyer_id))
            buyer = buy.scalar_one_or_none()
            return buyer

def get_all_buyers():
    async def get_buyer():
        async with async_session() as session:
            buy = await session.execute(select(Buyer))
            return buy

def post_buyer():
    async def add_buyer(item: BuyerSchema):
        new_buyer = Buyer(**dict(item))
        async with async_session() as session:
            session.add(new_buyer)
            await session.commit()
        return item