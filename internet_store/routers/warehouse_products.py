from fastapi import APIRouter
from internet_store import controllers
from internet_store.schemas.warehouse_products import Warehouse_ProductSchema

router = APIRouter(prefix="/warehouse_products")

@router.get('/{warehouse_products_id}')
async def get_warehouse_products(warehouse_products_id: int):
     return await controllers.get_warehouse_product(warehouse_products_id)

@router.post('/create')
async def add_warehouse_products(item: Warehouse_ProductSchema):
     return await controllers.post_warehouse_product(item)