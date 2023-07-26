from fastapi import APIRouter
from internet_store import controllers
from internet_store.schemas.vendors import VendorSchema

router = APIRouter(prefix="/vendors")


@router.get('/{vendor_id}')
async def get_vendor(vendor_id: int):
    return await controllers.get_vendor(vendor_id)

@router.post('/create')
async def add_vendor(item: VendorSchema):
    return await controllers.post_vendors(item)
