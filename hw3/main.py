#!/usr/bin/env python3

import asyncio
from aiohttp import ClientSession
from asyncpgsa import pg
import models
import os


async def fetch_json(session: ClientSession, url: str) -> dict:
    """
    :param session:
    :param url:
    :return:
    """
    async with session.get(url) as response:
        return await response.json()


async def getuser(id=None):
    """
    :param id:
    :return:
    """
    if id is None:
        url = 'https://jsonplaceholder.typicode.com/users'
    else:
        url = f'https://jsonplaceholder.typicode.com/users/{id}/'

    async with ClientSession() as session:
        result = await fetch_json(session, url)


async def getpost(id=None):
    """
    :param id:
    :return:
    """
    if id is None:
        url = 'https://jsonplaceholder.typicode.com/posts'
    else:
        url = f'https://jsonplaceholder.typicode.com/posts/{id}/'

    async with ClientSession() as session:
        result = await fetch_json(session, url)

async def main():
    tbl_user = models.tbl_user
    tbl_post = models.tbl_post

    await pg.init(
        os.getenv('PG_CONN'),
        min_size=3,
        max_size=5,
    )

    post_query = tbl_post.select()
    async with pg.query(post_query) as cursor:
        async for res in cursor:
            print(res)

    user_query = tbl_user.select()
    async with pg.query(user_query) as cursor:
        async for res in cursor:
            print(res)

    return 1

if __name__ == '__main__':
    print('Start!')
    asyncio.run(main())