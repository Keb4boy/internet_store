from internet_store.models import Product
from sqlalchemy.future import select
from internet_store.main import *
from internet_store.database import async_session, engine

async def get_product(product_id):
    async with engine.connect() as session:
        product = await session.execute(select(Product).where(Product.id == product_id))
        data = product.all()
        result = {}
        result.update(data)
    return result.__dict__

async def post_product(item):
    new_product = Product(**dict(item))
    async with async_session() as session:
        session.add(new_product)
        await session.commit()
    return item