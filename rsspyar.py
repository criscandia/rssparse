# -*- coding: utf-8 -*

#Leer detalle libreria io
import io
import feedparser
import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.MIMEMultipart import MIMEMultipart
from email.mime.text import MIMEText
import re
import sys
sys.path.append('/home/crisian/Dropbox/rssparse')
from auth import *
from datetime import datetime

#Creo la ruta del .txt con la data, recorro el rss y escribo el archivo

myfile="/home/crisian/Dropbox/rssparse/rssparse/rss.txt"
d = feedparser.parse('https://remoteok.io/remote-jobs.rss')

for posts in d.entries:
    print posts.title + ": " + posts.link + "\n"
    f = open("rss.txt", "a")
    f.write(str(posts.title) + ": " + str(posts.link) +'\n')
    f.truncate()

#Configuro los destinatarios

fromaddr = 'cristian.candia@devecoop.com'
toaddrs = 'cristian.candia@devecoop.com'
msg = MIMEMultipart()
now = datetime.now()
date = now.strftime('%d %b %Y %X')
msg["Subject"] = "Listado de Proyectos Remote OK"+ ', ' + date
f = open("rss.txt")
attachment = MIMEText(f.read())
attachment.add_header('Content-Disposition', 'attachment',
                      filename="/home/crisian/Dropbox/rssparse/rssparse/rss.txt")
msg.attach(attachment)

#Hago el envío de mail

server = smtplib.SMTP('smtp.gmail.com', 587)
server.ehlo()
server.starttls()
server.ehlo()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg.as_string())
server.quit()

#Borro el TXT del directorio

if os.path.isfile(myfile):
    os.remove(myfile)
else:
    print("Error: %s file not found" % myfile)




