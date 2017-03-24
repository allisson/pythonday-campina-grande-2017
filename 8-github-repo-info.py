import time
import paco
import aiohttp
from github import REPOS, ACCESS_TOKEN


async def get_repo_info(repo_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(repo_url, params={'access_token': ACCESS_TOKEN}) as response:
            response_data = await response.json()
            repo_info = {
                'name': response_data['name'],
                'full_name': response_data['full_name'],
                'stargazers_count': response_data['stargazers_count']
            }
            print(repo_info)

start = time.time()
tasks = [get_repo_info(repo_url) for repo_url in REPOS]
paco.run(paco.wait(tasks, limit=10))
end = time.time()
print('Tempo de execução={:.2f} segundos'.format(end - start))
