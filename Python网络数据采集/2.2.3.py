#bs中的有用的解析，子标签，后代标签，兄弟标签，父标签
from urllib.request import  urlopen
from bs4 import  BeautifulSoup

html=urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj=BeautifulSoup(html,"html.parser")
print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
