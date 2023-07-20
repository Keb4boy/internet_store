from sqlalchemy import Column, String, Integer, ForeignKey, VARCHAR, Float
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy_utils import PhoneNumberType, EmailType


class BaseModel(DeclarativeBase):
    id = Column(Integer, primary_key=True)


class Vendor(BaseModel):
    __tablename__ = "vendors"

    name = Column(VARCHAR(255), nullable=False)


class Warehouse(BaseModel):
    __tablename__ = "warehouses"

    geo = Column(VARCHAR(255), nullable=False)

    vendor_id = Column(Integer, ForeignKey("vendors.id"))


class Product(BaseModel):
    __tablename__ = "products"

    name = Column(VARCHAR(255), nullable=False)
    price = Column(Float, nullable=False)


class Warehouse_product(BaseModel):
    __tablename__ = "warehouse_products"

    warehouses_id = Column(Integer, ForeignKey("warehouses.id"))
    produts_id = Column(Integer, ForeignKey("products.id"))
    amount = Column(Integer, nullable=False)


class Buyer(BaseModel):
    __tablename__ = "buyers"

    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(EmailType(), nullable=False)
    password = Column(String, nullable=False)
    login = Column(String, nullable=False)


class Order(BaseModel):
    __tablename__ = "orders"

    buyers_id = Column(ForeignKey("buyers.id"))


class Orders_product(BaseModel):
    __tablename__ = "orders_products"

    order_id = Column(ForeignKey("orders.id"))
    products_id = Column(ForeignKey("products.id"))
    count = Column(Integer, nullable=False)
    price = Column(Float, nullable=False)
