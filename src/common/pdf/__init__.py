# -*- encoding: utf-8 -*-

from urllib.request import urlopen
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, process_pdf
from pdfminer.converter import TextConverter
from pdfminer.layout import  LAParams

# 读取pdf的函数，返回内容
def readPdf(pdf_file):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    laparams = LAParams()
    device = TextConverter(rsrcmgr=rsrcmgr, outfp=retstr, laparams=laparams)

    process_pdf(rsrcmgr=rsrcmgr, device=device, fp=pdf_file)
    device.close()

    content = retstr.getvalue()
    retstr.close()
    return content


url = "http://www.pythonscraping.com/pages/warandpeace/chapter1.pdf"
pdf_file = open(r'D:\Users\sunpj\Desktop\1.pdf','rb') # 也可以换成本地pdf文件，用open rb模式打开
content = readPdf(pdf_file)
print(content)
pdf_file.close()