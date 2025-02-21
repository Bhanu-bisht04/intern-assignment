import smtplib
import os
from email.message import EmailMessage

SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "bhanupratapsinghbisht8@gmail.com"
SENDER_PASSWORD = "hukg cbte sgrf jvzm"
RECIPIENT_EMAIL = "bhanupratapsinghbisht8@gmail.com"

subject = "Challenge 3 Completed"
body = """\
Name: Bhanu Bisht
Semester: 8
Branch: CSE
Roll Number: 13
"""
image_path = " image.jpg"

allowed_extensions = {".png", ".jpg", ".jpeg"}
file_extension = os.path.splitext(image_path)[1].lower()

if file_extension not in allowed_extensions:
    raise ValueError("Only PNG, JPG, and JPEG files are allowed.")

msg = EmailMessage()
msg["From"] = SENDER_EMAIL
msg["To"] = RECIPIENT_EMAIL
msg["Subject"] = subject
msg.set_content(body)

with open(image_path, "rb") as img_file:
    img_data = img_file.read()
    msg.add_attachment(img_data, maintype="image", subtype=file_extension[1:], filename=os.path.basename(image_path))

# Send email
try:
    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()  # Secure the connection
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.send_message(msg)
        print("Email sent successfully!")
except Exception as e:
    print(f"Error: {e}")