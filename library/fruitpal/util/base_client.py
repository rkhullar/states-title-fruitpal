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

    def get(self, uri: str, params: dict = None, **kwargs):
        params = {key: val for key, val in params.items() if val is not None}
        return httpx.get(url=self.path(uri), params=params, **kwargs)

    def post(self, uri: str, **kwargs):
        return httpx.post(url=self.path(uri), **kwargs)
