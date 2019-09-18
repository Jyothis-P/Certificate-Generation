from PyPDF2 import PdfFileWriter, PdfFileReader
import io

from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

# Adding custom fonts. 1st parm is the name of the font and 2nd is the path to the ttf font file.
pdfmetrics.registerFont(TTFont('Roboto', 'RobotoMono-Medium.ttf'))
pdfmetrics.registerFont(TTFont('RobotoL', 'RobotoMono-Light.ttf'))


# Function to return a pdf page with the parameters added into it.
def createpage(name, seat, food):
    packet = io.BytesIO()
    can = canvas.Canvas(packet)
    
    
    can.setFont('Roboto', 70)                # Setting the font and size of text.
    can.drawString(300, 925, name)           # Drawing a string onto the page. (x, y, string)

    can.setFont('RobotoL', 48)
    can.drawString(2110, 925, name)
    can.drawString(2110, 785, seat)
    can.drawString(2110, 648, food)

    can.setFont('RobotoL', 60)
    can.drawString(1600, 648, seat)

    # =======================================================================================================
    # Code to centre a string between a starting and ending coordinates.

    can.setFont('Roboto', 17)

    # You'll have to determine the following values with the help of the helper file, get_pdf_coordinates.py
    start = 210
    end = 646
    length_of_one_letter = 10               # Use some 'monospaced' font so that each letter will have the same length.
    y = 280

    mid = start + (end - start)/2
    half_string_size = (len(name)/2)*length_of_one_letter
    x = mid - half_string_size
    can.drawString(x, y, name)
    # =======================================================================================================
    

    can.save()                               # Save the canvas


    packet.seek(0)
    # Creating a pdf with just the canvas we just created.
    new_pdf = PdfFileReader(packet)

    # Read your existing PDF (ticket.pdf)
    existing_pdf = PdfFileReader(open("ticket.pdf", "rb"))
    # Add the canvas on the existing page
    page = existing_pdf.getPage(0)
    page2 = new_pdf.getPage(0)
    page.mergePage(page2)

    return page


if __name__=="__main__":
    output = PdfFileWriter()

    page = createpage("JERIN","#A10", "VEG")
    output.addPage(page)                     # Adding that page to the pdf.
    
    # Writing it to a file.
    outputStream = open("certificate.pdf", "wb")
    output.write(outputStream)
    outputStream.close()