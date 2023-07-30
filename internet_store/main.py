from fastapi import FastAPI
from internet_store.routers.vendors import router as router_vendor
from internet_store.routers.buyer import router as router_buyer
from internet_store.routers.orders import router as router_order
from internet_store.routers.orders_product import router as router_orders_product
from internet_store.routers.warehouse import router as router_warehouse
from internet_store.routers.warehouse_products import router as router_warehouse_products
from internet_store.routers.products import router as router_products


app = FastAPI()

app.include_router(router_buyer) 
app.include_router(router_order) 
app.include_router(router_orders_product) 
app.include_router(router_products) 
app.include_router(router_warehouse) 
app.include_router(router_vendor) 
app.include_router(router_warehouse_products) 