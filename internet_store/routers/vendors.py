from fastapi import APIRouter
from internet_store import controllers

router = APIRouter(prefix="/vendors")


@router.get('/{vendor_id}')
async def get_vendor(vendor_id: int):
    return controllers.get_vendor(vendor_id)

# async def add_vendor(item: VendorSchema):
# @router.post('/create')
# async def add_vendor()