import time
import multiprocessing
import requests
from github import REPOS, ACCESS_TOKEN


def grab_data_from_queue():
    while not q.empty():
        repo_url = q.get()
        response = requests.get(repo_url, params={'access_token': ACCESS_TOKEN}).json()
        repo_info = {
            'name': response['name'],
            'full_name': response['full_name'],
            'stargazers_count': response['stargazers_count']
        }
        print(repo_info)
        q.task_done()


workers = 5
start = time.time()
q = multiprocessing.JoinableQueue()

for repo_url in REPOS:
    q.put(repo_url)

for i in range(workers):
    process = multiprocessing.Process(target=grab_data_from_queue)
    process.start()

q.join()
end = time.time()
print('Tempo de execução={:.2f} segundos'.format(end - start))
