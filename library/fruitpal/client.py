from dataclasses import dataclass

from .util import async_httpx


@dataclass
class FruitPalClient:
    base_url: str

    async def create_vendor(self):
        pass

    async def read_vendors(self):
        pass

    async def estimate(self):
        pass
