from fastapi import APIRouter
from internet_store import controllers
from internet_store.schemas.orders_product import Orders_ProductSchema

router = APIRouter(prefix="/orders_product")

@router.post('/create')
async def add_orders_product(item: Orders_ProductSchema):
     return await controllers.post_orders_product(item)

@router.get('/{orders_product}')
async def get_orders_product(orders_product: int):
     return await controllers.get_orders_product(orders_product)
