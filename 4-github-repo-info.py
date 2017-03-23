import time
from concurrent import futures
import requests
from github import REPOS, ACCESS_TOKEN


def get_repo_info(repo_url):
    response = requests.get(repo_url, params={'access_token': ACCESS_TOKEN}).json()
    repo_info = {
        'name': response['name'],
        'full_name': response['full_name'],
        'stargazers_count': response['stargazers_count']
    }
    print(repo_info)


workers = 5
start = time.time()

with futures.ThreadPoolExecutor(workers) as executor:
    executor.map(get_repo_info, REPOS)

end = time.time()
print('Tempo de execução={:.2f} segundos'.format(end - start))
