from models.database import db
from sqlalchemy import Column, Integer, String, Numeric


class Menu(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True, nullable=False, server_default="", default="")
    cost = Column(Numeric, nullable=False, default=0)
