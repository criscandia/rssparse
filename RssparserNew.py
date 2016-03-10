# -*- coding: utf-8 -*


import ConfigParser
import io
import os
import re
import smtplib
import sys
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.MIMEMultipart import MIMEMultipart
from optparse import OptionParser

import feedparser


def sendmail(content):
    msg = MIMEMultipart()
    now = datetime.now()
    date = now.strftime('%d %b %Y %X')
    msg["Subject"] = "Listado de Proyectos Filtrados"+ ', ' + date
    attachment = MIMEText(content.encode('utf-8'))
    attachment.add_header('Content-Disposition', 'attachment',
                        filename="rss_laburos.txt")
    msg.attach(attachment)
    unexpanded_path = os.path.join("~", ".config", "rssparser.cfg")
    expanded_path = os.path.expanduser(unexpanded_path)
    config = ConfigParser.RawConfigParser()
    config.read(expanded_path)

    username = config.get('main', 'username')
    password = config.get('main', 'password')
    fromaddr = config.get('main', 'fromaddr')
    toaddrs = config.get('main', 'toaddrs')

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg.as_string())
    server.quit()


def parse(url_feed):
    posts = feedparser.parse(url_feed)
    content = ""
    tags = ['angular','node','nodejs','python', 'django','frontend','backend','remote']
    try:
        for post in posts.entries:
            if any(tag in post.title.lower() for tag in tags):       
                    link  = u"{}: {}\n".format(post.title, post.link)
                    content += link
            else: content
    except Exception, err:
        print "Failed to process link {}".format("Link")        
    return content



if __name__=="__main__":
    feed_option = "url_feed"
    parser = OptionParser()
    parser.add_option("-f", "--feed", dest=feed_option,
                  help="write report to FILE", metavar="FILE")

    (options, args) = parser.parse_args()
    if options.url_feed:
    #url_feed = 'http://python.org.ar/trabajo/rss'
        content = parse(options.url_feed)
        if content != "":
            sendmail(content)
    else:
        print "Usage rssparser.py -f URL"
