from dataclasses import dataclass, field
from urllib.parse import urljoin

import httpx


@dataclass
class BaseClient:
    host: str
    port: int = field(default=443, repr=False)
    protocol: str = field(default='https', repr=False)
    prefix: str = field(default='/api/v1/', repr=False)

    def path(self, uri: str) -> str:
        return urljoin(f'{self.protocol}://{self.host}:{self.port}', f'{self.prefix}{uri}')

    def get(self, uri: str, **kwargs):
        return httpx.get(url=self.path(uri), **kwargs)

    def post(self, uri: str, **kwargs):
        return httpx.post(url=self.path(uri), **kwargs)
