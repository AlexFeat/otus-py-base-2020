#!/usr/bin/env python3

import asyncpg
import asyncio

print('Start!')

async def main():
    conn = await asyncpg.connect(
        'postgres://uulbmfbi:kwLmeN2XgDLI7kk0iEYrHJ2A5s6Y_up1@dumbo.db.elephantsql.com:5432/uulbmfbi'
    )
    await conn.close()
    return 1

if __name__ == '__main__':
    print(asyncio.run(main()))