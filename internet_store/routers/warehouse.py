from fastapi import APIRouter
from internet_store import controllers
from internet_store.schemas.warehouse import WarehouseSchema

router = APIRouter(prefix="/warehouse")

@router.post('/create')
async def add_warehouse(item: WarehouseSchema):
     return await controllers.post_warehouse(item)

@router.get('/{warehouse_id}')
async def get_warehouse(warehouse_id: int):
     return await controllers.get_warehouse(warehouse_id)

