import os
from typing import Optional

from pydantic import BaseSettings


class ProjectSettings(BaseSettings):
    project: str = os.getenv('PROJECT', 'fruitpal')
    environment: Optional[str] = os.getenv('ENVIRONMENT')
    debug = bool(os.getenv('DEBUG', 0))


class NetworkSettings(BaseSettings):
    service_host: str = os.getenv('SERVICE_HOST', '0.0.0.0')
    service_port: int = int(os.getenv('SERVICE_PORT', '8000'))


class SQLiteSettings(BaseSettings):
    pass


class Settings(ProjectSettings, NetworkSettings, SQLiteSettings):
    pass
