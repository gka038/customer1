import requests
import json
import sys
import re

headers = {'Accept': 'application/vnd.github.v3+json'}
open_pull_requests = requests.get('https://api.github.com/repos/gka038/buffer-repo/pulls?state=open', headers=headers).json()

for obj in open_pull_requests:
    pr_num = str(obj['number'])
    print("PR is open on buffer repo: ", pr_num)
    url='https://api.github.com/repos/gka038/buffer-repo/pulls/'+ pr_num +'/files'
    pr_details = requests.get(url).json()
    for item in pr_details:
        file_changed = item["filename"]
        print("files changes on PR ", pr_num , " for file ", file_changed)
        if file_changed.startswith('customer1'):
            sys.exit('There is an open PRs on Buffer repo for this customer. Please close that to proceed')


print("No file conflicts on this customer in buffer repo PRs")

