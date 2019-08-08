import PyPDF2

file=open("C:\\Users\\lts\\PycharmProjects\\Test_Automation\\Directory_pdf\\doc.pdf",'rb')

pdfreader = PyPDF2.PdfFileReader(file)

print(pdfreader.getNumPages())

pageobj = pdfreader.getPage(0)
print(pageobj.extractText())

file.close()

