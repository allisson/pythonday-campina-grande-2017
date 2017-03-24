import asyncio
import aiomcache

loop = asyncio.get_event_loop()


async def main():
    mc = aiomcache.Client('127.0.0.1', 11211, loop=loop)
    await mc.set(b'key', b'hello world')
    value = await mc.get(b'key')
    print(value)

loop.run_until_complete(main())
