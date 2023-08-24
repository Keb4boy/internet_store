from fastapi import APIRouter, Query
from internet_store import controllers
from internet_store.schemas.vendors import VendorSchema
from typing import List

router = APIRouter(prefix="/vendors")

@router.get('/all/', response_model=List[VendorSchema])
async def get_all_vendor(offset: int = 0, limit: int = Query(default=3, lt=3)):
    return await controllers.get_all_vendor(offset, limit)

@router.post('/create')
async def add_vendor(item: VendorSchema):
    return await controllers.post_vendors(item)

@router.get('/{vendor_id}')
async def get_vendor(vendor_id: int):
    return await controllers.get_vendor(vendor_id)


