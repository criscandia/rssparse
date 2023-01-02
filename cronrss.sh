#!/bin/bash

#Activate virtualenv

cd ~/Documents/Programs/Projects/rssparse

source env/bin/activate

#Execute script rssparse

python3 RssparserNew.py -f http://python.org.ar/trabajo/rss
python3 RssparserNew.py -f https://remoteok.io/remote-jobs.rss
python3 RssparserNew.py -f https://dribbble.com/jobs.rss?location=Anywhere
python3 RssparserNew.py -f https://jobspresso.co/?feed=job_feed&job_types=developer&search_location&job_categories&search_keywords
python3 RssparserNew.py -f https://rss.indeed.com/rss?q=development
python3 RssparserNew.py -f https://rss.indeed.com/rss?q=javascript
python3 RssparserNew.py -f https://rss.indeed.com/rss?q=react 
python3 RssparserNew.py -f https://rss.indeed.com/rss?q=python
python3 RssparserNew.py -f https://rss.indeed.com/rss?q=engineer
python3 RssparserNew.py -f https://rss.indeed.com/rss?q=developer
python3 RssparserNew.py -f https://rss.indeed.com/rss?q=devops
python3 RssparserNew.py -f https://rss.indeed.com/rss?q=devs 
python3 RssparserNew.py -f https://www.remotepython.com/latest/jobs/feed/
python3 RssparserNew.py -f https://jobs.adafruit.com/wpjobboard/xml/rss/?query=&amp;location=&amp;type%5B%5D=7%22
python3 RssparserNew.py -f https://www.golangprojects.com/rss.xml
python3 RssparserNew.py -f https://hasjob.co/feed
python3 RssparserNew.py -f https://www.krop.com/services/feeds/rss/latest/




