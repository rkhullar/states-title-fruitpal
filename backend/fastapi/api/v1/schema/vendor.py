from decimal import Decimal

from pydantic import BaseModel


class VendorBase(BaseModel):
    country: str
    commodity: str
    variable_overhead: Decimal


class VendorCreate(VendorBase):
    pass


class Vendor(VendorBase):
    class Config:
        orm_mode = True
