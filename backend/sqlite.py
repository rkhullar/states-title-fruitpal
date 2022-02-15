from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_path = Path(__file__).parent / 'local' / 'sqlite.db'
if database_path.parent.exists():
    database_path.parent.mkdir()

database_url = f'sqlite:///{database_path}'
engine = create_engine(database_url, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
