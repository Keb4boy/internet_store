from fastapi import APIRouter
from internet_store import controllers
from internet_store.schemas.products import ProductSchema

router = APIRouter(prefix="/products")

@router.get('/{product_id}')
async def get_products(product_id: int):
     return await controllers.get_product(product_id)

@router.post('/create')
async def add_products(item: ProductSchema):
     return await controllers.post_product(item)