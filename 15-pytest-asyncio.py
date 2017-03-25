import pytest
import aiohttp
from github import REPOS, ACCESS_TOKEN


async def get_repo_info(repo_url):
    async with aiohttp.ClientSession() as session:
        async with session.get(repo_url, params={'access_token': ACCESS_TOKEN}) as response:
            response_data = await response.json()
            return {
                'name': response_data['name'],
                'full_name': response_data['full_name'],
                'stargazers_count': response_data['stargazers_count']
            }


@pytest.mark.asyncio
async def test_get_repo_info_1():
    repo_info = await get_repo_info(REPOS[0])
    assert 'name' in repo_info
    assert 'full_name' in repo_info
    assert 'stargazers_count' in repo_info


def test_get_repo_info_2(event_loop):
    repo_info = event_loop.run_until_complete(get_repo_info(REPOS[0]))
    assert 'name' in repo_info
    assert 'full_name' in repo_info
    assert 'stargazers_count' in repo_info
