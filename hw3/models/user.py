#!/usr/bin/env python3

from datetime import datetime as dt
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    BIGINT,
    DateTime,
    VARCHAR,
)

_metadata = MetaData()

tbl_user = Table(
    'items',
    _metadata,
    Column('id', BIGINT, primary_key=True),
    Column('username', VARCHAR(32), nullable=False),
    Column('name', VARCHAR(128)),
    Column('email', VARCHAR(128), nullable=False),
    Column(
        "ts_modify",
        DateTime,
        nullable=False,
        default=dt.today().isoformat(),
        server_default=dt.today().isoformat()),
    schema="user",
)