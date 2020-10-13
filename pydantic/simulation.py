"""
Simulation model.
"""

from datetime import date
import orjson
from pydantic import (
    BaseModel,
)


def orjson_loads(values):
    return orjson.loads(values)


def orjson_dumps(values, *, default):
    # orjson.dumps returns bytes, to match standard json.dumps we need to decode
    return orjson.dumps(values, default=default).decode()


class Simulation(BaseModel):
    init_date: date
    end_date: date
    name: str
    id: str
    code: int

    class Config:
        json_loads = orjson_loads
        json_dumps = orjson_dumps
