#!/usr/bin/env python3

import asyncio
from datetime import datetime as dt
from asyncpgsa import pg
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    DateTime,
)


print('Start!')

metadata = MetaData()

tbl_posts = Table(
    '"post"."items"',
    metadata,
    Column("id", Integer, primary_key=True),
    Column("user_id", Integer, nullable=False),
    Column("title", String, nullable=False),
    Column("body", String, nullable=False, default="", server_default=""),
    Column("ts_modify", DateTime, nullable=False, default=dt.today().isoformat(), server_default=dt.today().isoformat()),
)

async def main():
    conn = await pg.init(
        'postgres://uulbmfbi:kwLmeN2XgDLI7kk0iEYrHJ2A5s6Y_up1@dumbo.db.elephantsql.com:5432/uulbmfbi',
        min_size=3,
        max_size=5,
    )
    post_query = tbl_posts.select()

    results = await pg.query(post_query)
    for res in results:
        print(res)

    await conn.close()
    return 1

if __name__ == '__main__':
    print(asyncio.run(main()))