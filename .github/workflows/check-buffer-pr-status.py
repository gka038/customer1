import requests
import json
import sys
import re

customer_pr_number = sys.argv[1]
headers = {'Accept': 'application/vnd.github.v3+json'}
open_pull_requests = requests.get('https://api.github.com/repos/gka038/buffer-repo/pulls?state=open', headers=headers).json()

for obj in open_pull_requests:
    pr_title = str(obj['title'])
    if pr_title == "source PR: https://github.com/gka038/customer1/pull/"+ str(current_pr_number):
        print("Buffer repo PR is still open.. please ensure its closed. PR number on buffer repo is: ", str(obj['number']))
        sys.exit('First resolve PR Number: ', str(obj['number']), ' on buffer repo')
