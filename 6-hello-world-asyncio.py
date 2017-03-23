import asyncio


async def hello_world(name):
    print('Hello World, {}!'.format(name))

loop = asyncio.get_event_loop()
tasks = []
for name in ('fulano', 'cicrano', 'beltrano'):
    task = asyncio.ensure_future(hello_world(name))
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
