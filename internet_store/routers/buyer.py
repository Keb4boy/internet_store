from fastapi import APIRouter
from internet_store import controllers
from internet_store.schemas.buyer import BuyerSchema

router = APIRouter(prefix="/buyer")

@router.get('/{buyer_id}')
async def get_buyer(buyer_id: int):
     return await controllers.get_buyer(buyer_id)

@router.post('/create')
async def add_buyer(item: BuyerSchema):
     return await controllers.post_buyer(item)
