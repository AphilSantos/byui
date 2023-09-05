import smtplib
from email.message import EmailMessage
import time
import csv
import ssl

password = "lhfspaztcqrewjuh"


def send_email(recipient_name, recipient_email, subject, body_template):
    # Email setup
    msg = EmailMessage()
    msg.set_content(body_template.replace("{name}", recipient_name).replace("{email}",recipient_email), subtype="html")
    msg["Subject"] = subject
    msg["From"] = "BYU-Pathway Peer Mentor"
    msg["To"] = recipient_email

    context = ssl.create_default_context()

    # Gmail SMTP settings
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("aaron.santos.mentor@gmail.com", "lhfspaztcqrewjuh")  

    # Sending email
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    subject = "Classes Starting on September 11 -- BYU-Pathway Worldwide"
    body_template = """
 <html>
 <body>   
    <p>Hello <strong>{name},</strong><p>
<br>
<p>How are doing this summer? By the way, my name is Aaron Santos and I am you Peer Mentor. I am living here in the Philippines and I am glad that I get to work with you this semester.</p>
<p>Classes are getting closer and closer! <strong>On the 11th of September,</strong> online courses will begin. As a BYU-Pathway student myself, I am having mixed feelings.
For one, I am getting nervous because I know that things will be challenging. What I am doing now is preparing by writing my schedule to make sure that I have time for school, my full-time job, and rest.
</p>
<p>
Although, it is normal to feel nervous and worried, I know by experience that we can make this fun! Not to mention that the Lord promised to provide for His saints because He simply wants us to be successful
especially in our righteous endeavors.
<br><br>
That said, I want you to know that I am here to assist you become successful in your educational journey here at BYU-Pathway Worldwide. Feel free to contact me whenever you encounter problems with the portal, schedules, 
or generally anything that has to do with you and the program.
</p>
<p>
How about you? How are you preparing for this coming semester?<br><br>
<img src="https://assets.churchofjesuschrist.org/ee/86/ee86018cde1b71b772466e60d26d8f7245d4c0f8/meme_holland_hope_journey.jpeg" alt="hope on journey on" style="max-width: 630px; height: auto;">
</p>
<br><br>
<p>Regards,<br><br>
--
<br><br>
<strong>Aaron Santos<br>
Peer Mentor</strong>
<br><br>
<strong>Whatsapp:</strong> (+63) 9532800922<br>
<strong>Facebook:</strong> <a href="https://www.facebook.com/aaronphil2z.santos/" target="_blank">https://www.facebook.com/aaronphil2z.santos/</a><br>
<strong>LinkedIn:</strong> <a href="https://www.linkedin.com/in/aaron-santos-a1561b22b/" target="_blank"> https://www.linkedin.com/in/aaron-santos-a1561b22b/ </a><br>
</p>
</body>

<style>
a {
color: blue;
}

</style>
</html>
"""
    
    with open('contacts.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            send_email(row["Name"], row["Email"], subject, body_template)
            print(f"Email sent to {row['Name']} at {row['Email']}")
            time.sleep(5)  
        print("All emails sent")