from dataclasses import asdict
from decimal import Decimal
from typing import TypeVar

T = TypeVar('T')


def to_dict(self: T) -> dict:
    # NOTE: workaround for encoding decimal to json
    data = asdict(self)
    for key in data.keys():
        if isinstance(data[key], Decimal):
            data[key] = float(data[key])
    return data


def from_dict(cls: type[T], data: dict) -> T:
    # NOTE: workaround for encoding decimal to json
    for key in data.keys():
        if isinstance(data[key], float):
            data[key] = Decimal(str(data[key]))
    return cls(**data)
