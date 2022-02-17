from dataclasses import dataclass
from decimal import Decimal

from .util import from_dict, to_dict


@dataclass
class Vendor:
    country: str
    commodity: str
    variable_overhead: Decimal

    def to_dict(self) -> dict:
        return to_dict(self)

    @classmethod
    def from_dict(cls, data: dict) -> 'Vendor':
        return from_dict(cls, data)


@dataclass
class Estimate:
    country: str
    purchase_cost: Decimal
