from fastapi import APIRouter
from .users.views import router as users_router
from .categories.views import router as categories_router
from .records.views import router as records_router

router = APIRouter()
router.include_router(router=users_router, prefix="/users")
router.include_router(router=categories_router, prefix="/categories")
router.include_router(router=records_router, prefix="/records")
