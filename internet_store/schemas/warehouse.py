from pydantic import BaseModel


class WarehouseSchema(BaseModel):
    geo: str
    vendor_id: int