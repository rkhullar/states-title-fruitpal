from decimal import Decimal

from sqlalchemy import desc
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


@router.post('/vendors', response_model=Vendor)
async def create_vendor(data: VendorCreate, db: Session = Depends(get_db)):
    # TODO: check doc already exists before creating
    return VendorInDB.create(db=db, **data.dict())


@router.get('/vendors', response_model=list[Vendor])
async def read_vendors(country: str = None, commodity: str = None, db: Session = Depends(get_db)):
    return VendorInDB.query(db=db, country=country, commodity=commodity)


@router.get('/estimate', response_model=list[Estimate])
async def estimate(commodity: str, unit_price: int, volume: int, db: Session = Depends(get_db)):
    vendors = db.query(VendorInDB).filter_by(commodity=commodity).order_by(desc(VendorInDB.variable_overhead)).all()
    purchase_costs = [vendor.calculate_purchase_cost(unit_price, volume) for vendor in vendors]
    return [
        Estimate(country=vendor.country, purchase_cost=purchase_cost)
        for vendor, purchase_cost in zip(vendors, purchase_costs)
    ]
