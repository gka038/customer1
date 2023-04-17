import requests
import json

headers = {'Accept': 'application/vnd.github.v3+json'}
open_pull_requests = requests.get('https://api.github.com/repos/gka038/customer1/pulls?state=all', headers=headers)

print(open_pull_requests)