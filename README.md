# Certificate-Generation

This is a program that allows you to insert names and other details into an certificate or any other pdf file.
After playing around a bit, you can easily create certificates for a list of people.

Packages Required
1. PyPDF2
2. reportlab

(for email)
3. email
4. smtplib
5. ssl

You can install them wih pip install <package-name>

Use the get_pdf_coordinates.py helper file to determine the coordinates, font size etc that you want to use.

Then create the certificates with create_certificate.py

You can also send this via mail using send.py
