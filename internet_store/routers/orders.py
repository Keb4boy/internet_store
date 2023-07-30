from fastapi import APIRouter
from internet_store import controllers
from internet_store.schemas.orders import OrderSchema

router = APIRouter(prefix="/orders")

@router.get('/{order_id}')
async def get_order(order_id: int):
     return await controllers.get_order(order_id)

@router.post('/create')
async def add_order(item: OrderSchema):
     return await controllers.post_order(item)

