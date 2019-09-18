import email, smtplib, ssl

from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

subject = "Tickets | TEDxCUSAT"
sender_email = "admin@tedxcusat.in"
password = "<insert password here>"
# password = input("Type your password and press enter:")


def mail(receiver_email, body):
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = "TEDxCUSAT <admin@tedxcusat.in>"
    # message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = sender_email  # Recommended for mass emails (sending one email to multiple recepients) Not our case.

    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "certificcate.pdf"  # In same directory as script

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtpout.asia.secureserver.net", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)

if __name__ == "__main__":
    receiver_email = "jyothisp52@gmail.com"
    body = "This is an email with attachment sent from Python"
    mail(receiver_email, body)