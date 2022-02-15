from pathlib import Path

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker

database_path = Path(__file__).parents[3] / 'local' / 'sqlite.db'
if not database_path.parent.exists():
    database_path.parent.mkdir()

database_url = f'sqlite:///{database_path}'
engine = create_engine(database_url, connect_args={'check_same_thread': False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
SQLiteBase = declarative_base()


def _build_extra(kls: type[SQLiteBase]):
    class DocumentExtras:
        @classmethod
        def create(cls, db: Session, **data) -> kls:
            doc = kls(**data)
            db.add(doc)
            db.commit()
            db.refresh(doc)
            return doc
    return DocumentExtras


def _inject(source: type, target: type, members: list[str]):
    for member in members:
        setattr(target, member, getattr(source, member))


def document_extras(cls: type[SQLiteBase]):
    to_inject = _build_extra(cls)
    _inject(source=to_inject, target=cls, members=['create'])
    return cls
