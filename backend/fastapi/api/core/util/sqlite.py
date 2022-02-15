from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database_path = Path(__file__).parents[3] / 'local' / 'sqlite.db'
if not database_path.parent.exists():
    database_path.parent.mkdir()

database_url = f'sqlite:///{database_path}'
print(database_url)
engine = create_engine(database_url, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SQLiteBase = declarative_base()
