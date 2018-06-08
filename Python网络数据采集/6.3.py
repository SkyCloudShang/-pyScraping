#读取csv文件,并打印出来
from urllib.request import urlopen
from io import StringIO
import csv

data=urlopen("http://www.pythonscraping.com/files/MontyPythonAlbums.csv").read().decode('ascii','ignore')
dataFile=StringIO(data)
csvReader=csv.reader(dataFile)

for row in csvReader:
    print(row)