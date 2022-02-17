from dataclasses import dataclass

from .model import Estimate, Vendor
from .util import BaseClient


@dataclass
class FruitPalClient(BaseClient):

    def create_vendor(self, **kwargs) -> Vendor:
        vendor = Vendor(**kwargs)
        response = self.post('vendors', json=vendor.to_dict())
        response.raise_for_status()
        data = response.json()
        return Vendor.from_dict(data)

    def read_vendors(self) -> list[Vendor]:
        pass

    def estimate(self) -> Estimate:
        pass
