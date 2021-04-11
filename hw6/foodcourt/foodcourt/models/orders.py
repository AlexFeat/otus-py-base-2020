from models.database import db
from datetime import datetime as dt
from sqlalchemy import Column, Integer, String, DateTime, Numeric


class Order(db.Model):
    id = Column(Integer, primary_key=True)
    ts_create = Column(DateTime, nullable=False, default=dt.utcnow, server_default='now()')
    item_list = Column(String, nullable=True)  # TODO fk or text array
    address = Column(String, nullable=False, default="", server_default="")
    count_person = Column(Integer, nullable=False, default=1)
    total_cost = Column(Numeric, nullable=False, default=0)
