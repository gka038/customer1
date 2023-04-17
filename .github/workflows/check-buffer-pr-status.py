import requests
import json
import sys
import re

customer_pr_number = sys.argv[1]
headers = {'Accept': 'application/vnd.github.v3+json'}
open_pull_requests = requests.get('https://api.github.com/repos/gka038/buffer-repo/pulls?state=all', headers=headers).json()

print("checking if buffer pr is merged")
for obj in open_pull_requests:
    pr_title = str(obj['title'])
    expected_title = "source PR: https://github.com/gka038/customer1/pull/"+ str(customer_pr_number)
    if pr_title == expected_title :
        if "".__eq__(str(obj['merged_at'])):
            sys.exit(0)
        else:
            sys.exit("The PR on buffer repo was not merged but closed. Please contact Ops team for more details")

sys.exit("The PR on buffer repo was not found. Please contact Ops team for more details")

