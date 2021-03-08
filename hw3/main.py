#!/usr/bin/env python3

import asyncio
from datetime import datetime as dt

from aiohttp import ClientSession
from asyncpgsa import pg
import models
import os


async def time_print(msg=None):
    print(f'[{dt.today().isoformat()}] {msg}')


async def fetch_json(session: ClientSession, url: str):
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
        await time_print('Collect Users from API')
    else:
        url = f'https://jsonplaceholder.typicode.com/users/{id}/'
        await time_print(f'Collect User from API by ID {id}')

    async with ClientSession() as session:
        result = await fetch_json(session, url)
    await time_print('Collect Users Done!')

    return result


async def getpost(id=None):
    """
    :param id:
    :return:
    """
    if id is None:
        url = 'https://jsonplaceholder.typicode.com/posts'
        await time_print('Collect Posts from API')
    else:
        url = f'https://jsonplaceholder.typicode.com/posts/{id}/'
        await time_print(f'Collect Post from API by ID {id}')

    async with ClientSession() as session:
        result = await fetch_json(session, url)
    await time_print('Collect Posts Done!')

    return result


async def main():
    tbl_user = models.tbl_user
    tbl_post = models.tbl_post

    users = {}
    posts = {}

    await pg.init(
        os.getenv('PG_CONN'),
        min_size=1,
        max_size=3,
    )

    post_query = tbl_post.select()
    async with pg.query(post_query) as cursor:
        async for res in cursor:
            row = dict(res)
            await time_print(f"Post '{row.get('title')}'({row['id']})")
            posts[row['id']] = row

    post_list = await getpost()
    for post in post_list:
        if posts.get(post.get('id')):
            continue
        await time_print(f"Post '{post.get('title')}'({post['id']}) in progress!")
        if post.get('userId') is not None and users.get(post.get('userId')) is None:
            user_query = tbl_user.select().where(tbl_user.c.id == post['userId'])
            usr = await pg.query(user_query)
            if usr is None or len(usr) == 0:
                external_usr = await getuser(post['userId'])
                usr_add = tbl_user.insert().values(
                    id=external_usr.get('id'),
                    name=external_usr.get('name'),
                    username=external_usr.get('username'),
                    email=external_usr.get('email'),
                )
                await pg.execute(usr_add)
                usr = await pg.query(user_query)
                if usr is None:
                    return Exception

            post_add = tbl_post.insert().values(
                id=post.get('id'),
                title=post.get('title'),
                body=post.get('body'),
                user_id=post.get('userId')
            )
            await pg.execute(post_add)

    return 1


if __name__ == '__main__':
    print(f'[{dt.today().isoformat()}] Start!')
    asyncio.run(main())
    print(f'[{dt.today().isoformat()}] Done!')
