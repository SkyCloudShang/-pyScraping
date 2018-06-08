#读取pdf文件
from urllib.request import urlopen
from pdfminer.pdfinterp import PDFResourceManager,process_pdf
from pdfminer.layout import LAParams
from pdfminer.converter import TextConverter
from io import StringIO
from io import open

def readPDF(pdfFile):
    rsrcmgr=PDFResourceManager()
    retstr=StringIO()
    laparams=LAParams()
    device=TextConverter(rsrcmgr,retstr,laparams=laparams)

    process_pdf(rsrcmgr,device,pdfFile)
    device.close()

    content=retstr.getvalue()
    retstr.close()
    return content

# pdfFile=urlopen("http://pythonscraping.com/pages/warandpeace/chapter1.pdf")
pdfFile=open(r"C:\Users\Administrator\Desktop\旭辉深度报告\研报\旭辉控股集团(00884)引入中国平安，股东结构改善.pdf",'rb')
outputString=readPDF(pdfFile)
print(outputString)
pdfFile.close()
