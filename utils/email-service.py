import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from utils.encryption import encrypt_link
import os

def send_verification_email(user_email, user_id):
    token = encrypt_link(user_email)
    verification_link = f"http://localhost:5000/auth/verify-email?token={token}&id={user_id}"

    msg = MIMEMultipart()
    msg['From'] = os.getenv('EMAIL_USER')
    msg['To'] = user_email
    msg['Subject'] = 'Email Verification'

    body = f"Click on the link to verify your email: {verification_link}"
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(os.getenv('EMAIL_USER'), os.getenv('EMAIL_PASS'))
            server.sendmail(msg['From'], msg['To'], msg.as_string())
    except Exception as e:
        print(f"Failed to send email: {str(e)}")
