from dataclasses import dataclass
from .model import Vendor, Estimate
from urllib.parse import urljoin

from .util import async_httpx


@dataclass
class FruitPalClient:
    base_url: str

    def path(self, uri: str) -> str:
        # TODO: strip leading slash first
        return urljoin(self.base_url, f'/api/v1/{uri}')

    async def _get(self, uri: str, **kwargs):
        return await async_httpx(method='get', url=self.path(uri), **kwargs)

    async def _post(self, uri: str, **kwargs):
        return await async_httpx(method='post', url=self.path(uri), **kwargs)

    async def create_vendor(self):
        pass

    async def read_vendors(self):
        pass

    async def estimate(self):
        pass
