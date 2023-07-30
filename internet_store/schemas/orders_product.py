from pydantic import BaseModel


class Orders_ProductSchema(BaseModel):
    order_id: int
    products_id: int
    count: int
    price: int
