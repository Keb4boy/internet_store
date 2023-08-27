from pydantic import BaseModel


class BuyerSchema(BaseModel):
    
    first_name: str
    last_name: str
    phone: str
    email: str
    password: str
    login: str