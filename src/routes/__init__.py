from fastapi import APIRouter

# Routes
from src.routes.products import router as products_router 

router = APIRouter()
router.include_router(products_router)
