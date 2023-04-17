import requests
import json
import sys
import re

customer_pr_number = sys.argv[1]
headers = {'Accept': 'application/vnd.github.v3+json'}
open_pull_requests = requests.get('https://api.github.com/repos/gka038/buffer-repo/pulls?state=open', headers=headers).json()

print("checking if buffer pr is still open")
for obj in open_pull_requests:
    pr_title = str(obj['title'])
    expected_title = "source PR: https://github.com/gka038/customer1/pull/"+ str(customer_pr_number)
    if pr_title == expected_title :
        print("Buffer repo PR is still open.. please ensure its closed. PR number on buffer repo is: ", str(obj['number']))
        error_message = 'First resolve PR Number: '+ str(obj['number']) +' on buffer repo'
        sys.exit(error_message)

print("checking if buffer repo pr is merged")
closed_pull_requests = requests.get('https://api.github.com/repos/gka038/buffer-repo/pulls?state=closed', headers=headers).json()
for obj in closed_pull_requests:
    pr_title = str(obj['title'])
    expected_title = "source PR: https://github.com/gka038/customer1/pull/"+ str(customer_pr_number)
    if pr_title == expected_title :
        if str(obj['merged_at']) != null:
            sys.exit(0)
        else:
            sys.exit("The PR on buffer repo was not merged but closed. Please contact Ops team for more details")

