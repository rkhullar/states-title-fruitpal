from dataclasses import dataclass, field
from functools import cached_property
from urllib.parse import urljoin, urlparse

import httpx


@dataclass
class BaseClient:
    host: str
    port: int = field(default=None, repr=False)
    scheme: str = field(default='https', repr=False)
    prefix: str = field(default='/', repr=False)

    def __post_init__(self):
        self.prefix = self.prefix or '/'
        self.prefix = '/' + self.prefix.lstrip('/')
        self.prefix = self.prefix.rstrip('/') + '/'

    @classmethod
    def from_url(cls, url: str) -> 'BaseClient':
        parsed = urlparse(url)
        scheme = parsed.scheme if parsed.scheme else None
        prefix = parsed.path
        netloc_arr = parsed.netloc.split(':')
        host = netloc_arr[0]
        port = int(netloc_arr[1]) if len(netloc_arr) > 1 else None
        return cls(host=host, port=port, scheme=scheme, prefix=prefix)

    @cached_property
    def base_url(self) -> str:
        result = ''
        if self.scheme:
            result += f'{self.scheme}://'
        result += self.host
        if self.port:
            result += f':{self.port}'
        result += self.prefix
        return result

    def path(self, uri: str) -> str:
        return urljoin(self.base_url, uri.lstrip('/'))

    def get(self, uri: str, params: dict = None, **kwargs):
        params = {key: val for key, val in params.items() if val is not None}
        return httpx.get(url=self.path(uri), params=params, **kwargs)

    def post(self, uri: str, **kwargs):
        return httpx.post(url=self.path(uri), **kwargs)
