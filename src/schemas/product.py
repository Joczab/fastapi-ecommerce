from typing import Optional

from pydantic import BaseModel, Field


class ProductBase(BaseModel):

    name: str = Field(min_length=3, description='El nombre del producto debe tener minimo tres (3) caracteres')
    description: str
    price: float


class ProductRead(ProductBase):
    id: int
    is_active: bool


class ProductCreate(ProductBase):
    pass


class ProductUpdate(BaseModel):

    name: Optional[str] = Field(default=None, min_length=3)
    description: Optional[str] = None
    price: Optional[float] = Field(default=None, gt=0)
    is_active: Optional[bool] = None
    