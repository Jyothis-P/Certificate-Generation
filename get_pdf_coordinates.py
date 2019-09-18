from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

pdfmetrics.registerFont(TTFont('Roboto', 'RobotoMono-Medium.ttf'))
# pdfmetrics.registerFont(TTFont('Robotomono', 'RobotoMono-Medium.ttf'))
packet = io.BytesIO()

# create a new PDF with Reportlab


def creatpdf(name, event):
    can = canvas.Canvas(packet)
    can.setFont('Roboto', 5)
    # can.setFont('Roboto', 70)

    
    # # To find the font size.
    # for x in range(20):
    #     can.setFont('Roboto', x*10)
    #     can.drawString(2000, x*100, str(x*10))
    # can.save()

   # To find the x and y axes.
    for x in range(1000):
       can.drawString(x*20, 640, str(x*20)) # x axis
       can.drawString(2110, x*20, str(x*20)) # y axis
    can.save()

    # move to the beginning of the StringIO buffer
    packet.seek(0)
    new_pdf = PdfFileReader(packet)
    # read your existing PDF
    existing_pdf = PdfFileReader(open("ticket.pdf", "rb"))
    output = PdfFileWriter()
    # add the "watermark" (which is the new pdf) on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)
    output.addPage(page)
    # finally, write "output" to a real file
    outputStream = open("certificate.pdf", "wb")
    output.write(outputStream)
    outputStream.close()

if __name__ =="__main__":
    creatpdf("SAHIL", "MAKE-A-TON")
