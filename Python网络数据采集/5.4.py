#用python发邮件
import smtplib
from email.mime.text import MIMEText
from urllib.request import urlopen
from bs4 import BeautifulSoup

def sendEmail(subject,body):
    msg=MIMEText(body)
    msg['Subject']=subject
    msg['From']="christmaas_alerts@pythonscraping.com"
    msg["to"]="ryan@pythonscraping.com"

    s=smtplib.SMTP('localhost')
    s.send_message(msg)
    s.quit()

bsObj=BaseException(urlopen("http://isitchristmas.com/"))

