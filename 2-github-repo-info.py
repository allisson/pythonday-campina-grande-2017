import time
import threading
import queue
import requests
from github import REPOS, ACCESS_TOKEN

max_threads = 5
start = time.time()
q = queue.Queue()


def load_queue():
    for repo_url in REPOS:
        q.put(repo_url)


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


load_queue()
for i in range(max_threads):
    thread = threading.Thread(target=grab_data_from_queue)
    thread.start()
q.join()
end = time.time()
print('Tempo de execução={:.2f} segundos'.format(end - start))
