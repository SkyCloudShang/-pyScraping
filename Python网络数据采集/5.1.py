import  os
from urllib.request import urlopen
from urllib.request import urlretrieve
from bs4 import BeautifulSoup

downLoadDirectory="downloaded"
baseUrl="http://pythonscraping.com"

def getAbsoluteURL(baseUrl,source):
    if source.startswith("http://www."):
        url="http://"+source[11:]
    elif source.startswith("http://"):
        url=source
    elif source.startswith("www."):
        url="http://"+source[4:]
    else:
        url=baseUrl+"/"+source
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl,absoluteUrl,downloadDirectory):
    path=absoluteUrl.replace("www.","")
    path=path.replace(baseUrl,"")
    path=downLoadDirectory+path
    directory=os.path.dirname(path)
    if not os.path.exists(directory):
        os.makedirs(directory)
    return 1

html=urlopen("http://www.pythonscraping.com")
bsObj=BeautifulSoup(html,"lxml")
downloadLists=bsObj.findAll(src=True)

for download in downloadLists:
    filrUrl=getAbsoluteURL(baseUrl,download["src"])
    if filrUrl is not None:
        print(filrUrl)
        # urlretrieve(filrUrl,filename="downloaded")
        urlretrieve(filrUrl,getDownloadPath(baseUrl,filrUrl,downLoadDirectory))
