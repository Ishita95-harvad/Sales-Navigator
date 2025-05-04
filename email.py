import smtplib
from email.mime.text import MIMEText
import os

def send_confirmation_email(recipient, name):
    sender = os.environ.get('EMAIL_USER')
    password = os.environ.get('EMAIL_PASS')
    subject = "Thank you for your submission"
    body = f"Hello {name},\n\nThanks for reaching out! We'll contact you soon."

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
        server.login(sender, password)
        server.send_message(msg)