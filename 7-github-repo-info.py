import time
import asyncio
import aiohttp
from github import REPOS, ACCESS_TOKEN


async def get_repo_info(loop, repo_url):
    async with aiohttp.ClientSession(loop=loop) as session:
        async with session.get(repo_url, params={'access_token': ACCESS_TOKEN}) as response:
            response_data = await response.json()
            repo_info = {
                'name': response_data['name'],
                'full_name': response_data['full_name'],
                'stargazers_count': response_data['stargazers_count']
            }
            print(repo_info)

start = time.time()
loop = asyncio.get_event_loop()
tasks = []
for repo_url in REPOS:
    task = asyncio.ensure_future(get_repo_info(loop, repo_url))
    tasks.append(task)
loop.run_until_complete(asyncio.wait(tasks))
end = time.time()
print('Tempo de execução={:.2f} segundos'.format(end - start))
