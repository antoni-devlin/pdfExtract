import PyPDF2
import re

path = 'ma-art-and-politics.pdf'

pdfFileObj = open(path, 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

pageObj = pdfReader.getPage(0)
results = pageObj.extractText()

chunk = str(results.replace('\n', ''))

results = re.findall('^.*?\([^\d]*(\d+)[^\d]*\).*$', chunk)[0]

print("The HECos code for this course is: " + results)
# print(type(results))
