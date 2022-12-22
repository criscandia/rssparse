#!/bin/bash

#Activate virtualenv

cd ~/Documents/Programs/Projects/rssparse

source env/bin/activate

#Execute script rssparse

python3 RssparserNewGdocs.py -f https://app.vuejobs.com/feed/posts
python3 RssparserNewGdocs.py -f https://landing.jobs/feed?remote=true
python3 RssparserNewGdocs.py -f https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss
python3 RssparserNewGdocs.py -f https://weworkremotely.com/categories/remote-back-end-programming-jobs.rss
python3 RssparserNewGdocs.py -f https://weworkremotely.com/categories/remote-front-end-programming-jobs.rss
python3 RssparserNewGdocs.py -f https://weworkremotely.com/categories/remote-devops-sysadmin-jobs.rss
python3 RssparserNewGdocs.py -f https://weworkremotely.com/categories/remote-full-stack-programming-jobs.rss


