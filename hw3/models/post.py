#!/usr/bin/env python3

from datetime import datetime as dt
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    BIGINT,
    Text,
    DateTime,
    VARCHAR,
)

_metadata = MetaData()

tbl_post = Table(
    'items',
    _metadata,
    Column("id", BIGINT, primary_key=True),
    Column("user_id", BIGINT, nullable=False),
    Column("title", VARCHAR(128), nullable=False),
    Column("body", Text, nullable=False, default="", server_default=""),
    Column(
        "ts_modify",
        DateTime,
        nullable=False,
        default=dt.today().isoformat(),
        server_default=dt.today().isoformat()),
    schema="post",
)