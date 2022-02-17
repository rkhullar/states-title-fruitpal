from collections.abc import Iterator
from dataclasses import dataclass
from decimal import Decimal

from .model import Estimate, Vendor
from .util import BaseClient


@dataclass
class FruitPalClient(BaseClient):

    def create_vendor(self, country: str, commodity: str, variable_overhead: Decimal) -> Vendor:
        vendor = Vendor(country=country, commodity=commodity, variable_overhead=variable_overhead)
        response = self.post('vendors', json=vendor.to_dict())
        response.raise_for_status()
        data = response.json()
        return Vendor.from_dict(data)

    def read_vendors(self, country: str = None, commodity: str = None) -> Iterator[Vendor]:
        response = self.get('vendors', params=dict(country=country, commodity=commodity))
        response.raise_for_status()
        for item in response.json():
            yield Vendor.from_dict(item)

    def estimate(self) -> Estimate:
        pass
