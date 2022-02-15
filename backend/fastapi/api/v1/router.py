from fastapi import APIRouter

from .routes import default

router = APIRouter()
router.include_router(default.router, prefix='', tags=[])
