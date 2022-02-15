from dataclasses import asdict, dataclass
from decimal import Decimal

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session

from ..core.util import SQLiteBase, document_extras


@dataclass
class Vendor:
    country: str
    commodity: str
    variable_overhead: Decimal

    def dict(self):
        return asdict(self)

    def calculate_purchase_cost(self, unit_price: int, volume: int) -> Decimal:
        return (unit_price + self.variable_overhead) * volume


@document_extras
class Hello(SQLiteBase):
    __tablename__ = 'hello'

    id = Column(Integer, primary_key=True, index=True)
    message = Column(String, unique=True, index=True)

    @classmethod
    def read(cls, db: Session):
        return db.query(cls).all()
