import asyncio
import aiopg
from speakers import SPEAKERS

dsn = 'dbname=pythonday user=pythonday password=pythonday host=127.0.0.1'


async def get_pool():
    return await aiopg.create_pool(dsn)


async def create_table():
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('DROP TABLE IF EXISTS speakers')
            await cur.execute('CREATE TABLE speakers (id serial PRIMARY KEY, name varchar(255))')
            for speaker in SPEAKERS:
                await cur.execute('INSERT INTO speakers (name) VALUES (%s)', (speaker,))


async def get_speakers():
    speakers = []
    pool = await get_pool()
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute('SELECT * FROM speakers')
            async for row in cur:
                speakers.append({'id': row[0], 'name': row[1]})
    return speakers


async def main():
    await create_table()
    speakers = await get_speakers()
    for speaker in speakers:
        print(speaker)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
