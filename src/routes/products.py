from fastapi import APIRouter

import src.models.product as db_products

from src.schemas.product import ProductRead, ProductCreate, ProductUpdate

router = APIRouter(tags=['Products'])


@router.get('/products')
def get_products():
    data = db_products.get_products()
    if not data:
        return {}
    return data


@router.post('/products', response_model=ProductRead)
def create_product(product: ProductCreate):
    return db_products.create_product(product.model_dump())


@router.put('/products/{product_id}')
def update_product(product_id: int, product: ProductUpdate):
    return db_products.update_product(product_id, product.model_dump(exclude_unset=True))


@router.delete('/products/{product_id}')
def delete_product(product_id: int):
    return db_products.delete_product(product_id)
