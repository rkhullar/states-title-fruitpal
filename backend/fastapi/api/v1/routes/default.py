from decimal import Decimal

from fastapi.encoders import jsonable_encoder

from ...core.router import APIRouter
from ...model import Vendor as VendorInDB
from ..schema import Vendor

vendor_database = [
   VendorInDB(country='MX', commodity='mango', variable_overhead=Decimal('1.24')),
   VendorInDB(country='BZ', commodity='mango', variable_overhead=Decimal('1.42'))
]


router = APIRouter()


@router.get('/vendors', response_model=list[Vendor])
async def list_vendors():
    def iter_vendors():
        for item in vendor_database:
            yield jsonable_encoder(Vendor(**item.dict()))
    return list(iter_vendors())


@router.post('/vendors', response_model=Vendor)
async def create_vendor(data: Vendor) -> Vendor:
    return jsonable_encoder(data)


@router.get('/estimate')
async def estimate(unit_price: int, volume: int):
    return dict(example=[
        {'country': 'MX', 'price': vendor_database[0].calculate_purchase_cost(unit_price, volume)},
        {'country': 'BZ', 'price': vendor_database[1].calculate_purchase_cost(unit_price, volume)}
    ])
