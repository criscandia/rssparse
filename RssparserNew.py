    # -*- coding: utf-8 -*


import configparser
import io
import os
import re
import smtplib
import sys
import urllib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from optparse import OptionParser
from email.mime.text import MIMEText
import csv
import feedparser
import pygsheets
import pandas as pd
import time

jobs = []
links = []
dates = []
gc = pygsheets.authorize(service_file="./gs_credentials.json")
    
def sendmail(content):
    msg = MIMEMultipart()
    now = datetime.now()
    date = now.strftime('%d %b %Y %X')
    part1 = MIMEText(content, "plain")
    msg["Subject"] = "Listado de Proyectos Filtrados"+ ', ' + date
    attachment = MIMEText(content.encode("utf8"), _subtype="plain", _charset="utf-8")
    attachment.add_header('Content-Disposition', 'attachment',
                        filename="rss_laburos.txt")
    msg.attach(attachment)
    msg.attach(part1)
    #for l in part1:
    #    print(content)
    unexpanded_path = os.path.join("rssparser.cfg")
    expanded_path = os.path.expanduser(unexpanded_path)
    config = configparser.RawConfigParser()
    config.read(expanded_path)

    username = config.get('main', 'username')
    password = config.get('main', 'password')
    fromaddr = config.get('main', 'fromaddr')
    toaddrs = config.get('main', 'toaddrs')
    ccaddr = config.get('main', 'ccaddr')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(fromaddr, (toaddrs, ccaddr), msg.as_string())
    server.quit()


def parse(url_feed):
    posts = feedparser.parse(url_feed)
    content = ""
    tags = ['angular','node','nodejs','python','django','frontend','backend','back end','remote','remoto','fullstack','js','.net','sap','azure','abap','react','reactnative','graphql','typescript','javascript','golang','vue', 'data']
    t = time.strptime('07/28/2014 18:54:55.099000', '%m/%d/%Y %H:%M:%S.%f')
    sevendays = 86400*7
    current = time.strftime ("%s",time.localtime())

    #print(posts)
    try:
        for post in list(filter(lambda post: any(location.lower() in post.summary.lower() for location in locations), posts.entries)):
            if any(tag in post.title.lower() and int(current) - time.mktime(t) > sevendays for tag in tags):
                    link  = "{}: {}\n".format(post.title, post.link)
                    jobs.append(post.title)
                    links.append(post.link)
                    dates.append(datetime.now().strftime('%d %b %Y %X'))
                    content += link
            else: content
    except Exception as err:
        print("Failed to process link {}".format("Link"))        
    return content

def sheet():
    df = pd.DataFrame()
    df["Date"] = dates
    df["Jobs"] = jobs
    df["Links"] = links
    sheet_name = str(datetime.now().year) + str(datetime.now().month)
    try:
        wks = gc.open("ListadoDeProyectos").worksheet_by_title(sheet_name)
    except Exception as err:
        file = gc.open("ListadoDeProyectos")
        file.add_worksheet(sheet_name)
        wks = file.worksheet_by_title(sheet_name)
    values = df.values.tolist()
    wks.append_table(values, start='A1', end=None, dimension='ROWS', overwrite=None)
    
if __name__=="__main__":
    feed_option = "url_feed"
    parser = OptionParser()
    parser.add_option("-f", "--feed", dest=feed_option,
                  help="write report to FILE", metavar="FILE")

    (options, args) = parser.parse_args()
    if options.url_feed:
    #url_feed = 'http://python.org.ar/trabajo/rss'
        content = parse(options.url_feed)
        print(jobs)
        sendmail(content)
        sheet()
    else:
        print ("Usage rssparser.py -f URL")




