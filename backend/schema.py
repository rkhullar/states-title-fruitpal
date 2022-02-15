from decimal import Decimal

from pydantic import BaseModel


class Vendor(BaseModel):
    country: str
    commodity: str
    variable_overhead: Decimal
