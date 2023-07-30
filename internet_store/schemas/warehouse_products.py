from pydantic import BaseModel


class Warehouse_ProductSchema(BaseModel):
    warehouses_id: int
    produts_id: int
    amount: int