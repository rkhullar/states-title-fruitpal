from decimal import Decimal
from sqlalchemy.orm import Session
from fastapi import Depends
from ...core.router import APIRouter
from ...model import Vendor as VendorInDB
from ..depends import get_db
from ..schema import *

vendor_database = [
   VendorInDB(country='MX', commodity='mango', variable_overhead=Decimal('1.24')),
   VendorInDB(country='BZ', commodity='mango', variable_overhead=Decimal('1.42'))
]


router = APIRouter()


@router.get('/vendors', response_model=list[Vendor])
async def list_vendors(db: Session = Depends(get_db)):
    return VendorInDB.read(db=db)


@router.post('/vendors', response_model=Vendor)
async def create_vendor(data: VendorCreate, db: Session = Depends(get_db)):
    return VendorInDB.create(db=db, **data.dict())


@router.get('/estimate')
async def estimate(unit_price: int, volume: int):
    return dict(example=[
        {'country': 'MX', 'price': vendor_database[0].calculate_purchase_cost(unit_price, volume)},
        {'country': 'BZ', 'price': vendor_database[1].calculate_purchase_cost(unit_price, volume)}
    ])
