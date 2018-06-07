from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random

pages=set()
random.seed(datetime.datetime.now())

#获取页面所有内链的列表
def getInternalLinks(bsObj,includeUrl):
    includeUrl=urlparse(includeUrl).scheme+"://"+urlparse(includeUrl).netloc
    internalLinks=[]
    for link in bsObj.findAll("a",href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] not in internalLinks:

#未完成 待续
