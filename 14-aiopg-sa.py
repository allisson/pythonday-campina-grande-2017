import asyncio
from aiopg.sa import create_engine
import sqlalchemy as sa
from speakers import SPEAKERS

metadata = sa.MetaData()
speakers_table = sa.Table(
    'speakers',
    metadata,
    sa.Column('id', sa.Integer, primary_key=True),
    sa.Column('name', sa.String(255))
)


async def get_engine():
    return await create_engine(
        user='pythonday', database='pythonday', host='127.0.0.1', password='pythonday'
    )


async def create_table():
    engine = await get_engine()
    async with engine.acquire() as conn:
        await conn.execute('DROP TABLE IF EXISTS speakers')
        await conn.execute('CREATE TABLE speakers (id serial PRIMARY KEY, name varchar(255))')
        for speaker in SPEAKERS:
            await conn.execute(speakers_table.insert().values(name=speaker))


async def get_speakers():
    speakers = []
    engine = await get_engine()
    async with engine.acquire() as conn:
        async for row in conn.execute(speakers_table.select()):
            speakers.append({'id': row.id, 'name': row.name})
    return speakers


async def main():
    await create_table()
    speakers = await get_speakers()
    for speaker in speakers:
        print(speaker)

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
