from pydantic import BaseModel


class OrderSchema(BaseModel):
    buyer_id: int