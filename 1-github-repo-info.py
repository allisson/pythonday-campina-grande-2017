import time
import requests
from github import REPOS, ACCESS_TOKEN

start = time.time()
for repo_url in REPOS:
    response = requests.get(repo_url, params={'access_token': ACCESS_TOKEN}).json()
    repo_info = {
        'name': response['name'],
        'full_name': response['full_name'],
        'stargazers_count': response['stargazers_count']
    }
    print(repo_info)
end = time.time()
print('Tempo de execução={:.2f} segundos'.format(end - start))
