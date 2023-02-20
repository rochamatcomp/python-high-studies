from datetime import date, datetime, time, timedelta
from pydantic import BaseModel


class Model(BaseModel):
    d: date = None
    dt: datetime = None
    t: time = None
    td: timedelta = None


print(Model.schema_json(indent=2))
