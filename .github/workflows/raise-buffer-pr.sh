#!/bin/bash

git clone https://github.com/gka038/buffer-repo.git
cd buffer-repo 
git checkout -b feat/customer1-pr-$1
cp -r ../env1/* customer1/env1/
cp -r ../env2/* customer1/env2/

git add --all
git commit -m "automatically raised PR from customer1 repo"

echo "trying to push now"
git push --set-upstream origin feat/customer1-pr-$1


