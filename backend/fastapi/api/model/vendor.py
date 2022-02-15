from decimal import Decimal

from sqlalchemy import Column, Float, Integer, String
from sqlalchemy.orm import Session

from ..core.util import SQLiteBase, document_extras


@document_extras
class Vendor(SQLiteBase):
    __tablename__ = 'vendors'

    country: str = Column(String, primary_key=True)
    commodity: str = Column(String, primary_key=True)
    variable_overhead: Decimal = Column(Float)

    @classmethod
    def read(cls, db: Session):
        return db.query(cls).all()

    def calculate_purchase_cost(self, unit_price: int, volume: int) -> Decimal:
        return (unit_price + self.variable_overhead) * volume
