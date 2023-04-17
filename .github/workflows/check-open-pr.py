import requests
import json
import sys

current_pr_number = sys.argv[1]

headers = {'Accept': 'application/vnd.github.v3+json'}
open_pull_requests = requests.get('https://api.github.com/repos/gka038/customer1/pulls?state=all', headers=headers)

print("current PR number is :", current_pr_number)
print(open_pull_requests)