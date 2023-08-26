import smtplib
from email.message import EmailMessage
import time
import csv
import ssl

password = "lhfspaztcqrewjuh"


def send_email(recipient_name, recipient_email, subject, body_template):
    # Email setup
    msg = EmailMessage()
    msg.set_content(body_template.replace("{name}", recipient_name).replace("{email}",recipient_email))
    msg["Subject"] = subject
    msg["From"] = "aaron.santos.mentor@gmail.com"
    msg["To"] = recipient_email

    context = ssl.create_default_context()

    # Gmail SMTP settings
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("aaron.santos.mentor@gmail.com", "lhfspaztcqrewjuh")  

    # Sending email
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    subject = "Hello there!"
    body_template = """Hello {name},

This is a test {name}. And your email address is {email}.

Regards,
Your Name
"""
    
    with open('contacts.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            send_email(row["Name"], row["Email"], subject, body_template)
            print(f"Email sent to {row['Name']} at {row['Email']}")
            time.sleep(5)  
        print("All emails sent")