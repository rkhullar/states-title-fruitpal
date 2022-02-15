from fastapi import APIRouter
from .routes import hello

router = APIRouter()
router.include_router(hello.router, prefix='/hello', tags=['hello'])
