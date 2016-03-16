#!/bin/bash

#Activate virtualenv

cd ~/virtualenv/rssparse
source bin/activate

#Execute script rssparse

python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f http://python.org.ar/trabajo/rss
python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f https://remoteok.io/remote-jobs.rss
python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f https://weworkremotely.com/categories/1/jobs.rss
python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f https://dribbble.com/jobs.rss?location=Anywhere
python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f https://jobspresso.co/?feed=job_feed&job_types=developer&search_location&job_categories&search_keywords
python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f https://weworkremotely.com/categories/2-programming/jobs.rss
python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f https://jobs.github.com/positions.atom
python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f http://feeds.feedblitz.com/flexjobs
python ~/Dropbox/rssparse/rssparse/RssparserNew.py -f http://careers.stackoverflow.com/jobs/feed?allowsremote=True


