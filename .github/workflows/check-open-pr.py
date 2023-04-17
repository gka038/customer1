import requests
import json
import sys

current_pr_number = sys.argv[1]

headers = {'Accept': 'application/vnd.github.v3+json'}
open_pull_requests = requests.get('https://api.github.com/repos/gka038/customer1/pulls?state=open', headers=headers).json()

print("current PR number is :", current_pr_number)

for obj in open_pull_requests:
    if str(obj['number']) == str(current_pr_number):
        open_pull_requests.pop()

if len(open_pull_requests) > 0:
    sys.exit('There are other open PRs on ths repo.. please wait for them to be resolved or closed')