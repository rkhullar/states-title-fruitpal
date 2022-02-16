from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Vendor:
    country: str
    commodity: str
    variable_overhead: Decimal


@dataclass
class Estimate:
    country: str
    purchase_cost: Decimal
