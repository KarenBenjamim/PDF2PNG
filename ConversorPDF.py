from PyPDF2 import PdfFileWriter, PdfFileReader
from pdf2image import convert_from_path
import os

def ListagemPDF(folder):
    lista = []
    for filename in os.listdir(folder):
        lista.append(folder+filename)
    return lista

Matricula = input("Matricula: ")
os.mkdir(Matricula)

PastaPDF = Matricula + "/PDF"
PastaPNG = Matricula + "/PNG"
os.mkdir(PastaPDF)
os.mkdir(PastaPNG)

inputpdf = PdfFileReader(open("Matricula_2_cod38898.pdf", "rb"))

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("%s/document-page%s.pdf" % (PastaPDF, i), "wb") as outputStream:
       output.write(outputStream)

lista = ListagemPDF('PDF/')

for i in range(len(lista)):
       img = convert_from_path("%s/document-page%s.pdf" % (PastaPDF, i) , dpi=200)

       for imgs in img:
              imgs.save("%s/document-page%s.png" % (PastaPNG, i), "PNG")

print("Conversão concluída.")