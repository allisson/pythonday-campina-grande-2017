import asyncio
import aioredis

loop = asyncio.get_event_loop()


async def main():
    redis = await aioredis.create_redis(('localhost', 6379), loop=loop)
    await redis.set('key', 'hello world')
    val = await redis.get('key')
    print(val)
    redis.close()
    await redis.wait_closed()

loop.run_until_complete(main())
