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
    msg["From"] = "Message from your Mentor"
    #msg["From"] = "Aaron Phil"
    msg["To"] = recipient_email

    context = ssl.create_default_context()

    # Gmail SMTP settings
    server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
    server.login("aaron.santos.mentor@gmail.com", "lhfspaztcqrewjuh")  
    #server.login("aphilvs@gmail.com", "qxrr mpxy zulc qqrn")
    # Sending email
    server.send_message(msg)
    server.quit()

if __name__ == "__main__":
    subject = "Have you decided on a Certificate?"
    body_template = """
<html>
<head>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; color: #333;">
    <div style="max-width: 600px; background-color: #fff; padding: 20px; border-radius: 8px; margin: auto;">
        <div style="font-size: 20px; font-weight: bold; margin-bottom: 15px;">Hi {name}!</div>
        
        <div style="line-height: 1.6; margin-bottom: 20px;">
           As your Mentor, I am here to answer any questions you may have about the certificate selection process and help you meet your educational/career goals. I am sending you the following survey to see how you feel about your certificate selection. 
        </div>

        <div style="line-height: 1.6; margin-bottom: 20px;">
            Which of the following options applies to you? :
            <ul>
                <li>A. I am confident in the certificate I have chosen.</li>

                <li>B. I am not confident that I chose the right certificate and want to know more about the certificate I chose. </li>

                <li>C. I am not confident in my certificate and I might choose another certificate.</li>

                <li>D. I have not chosen a certificate.</li>

                <li>E. I do not fully understand what a certificate is.</li>
            </ul>
             Please respond with the letter that best applies to your situation. If you are struggling to choose a certificate or have any questions, I would love to talk with you about this or any other challenges you may be facing. 
        </div>   


        <div style="line-height: 1.6; margin-bottom: 20px;">
          <b>5 TIPS FOR CHOOSING A CERTIFICATE</b> <br>
          Follow these suggestions from fellow students to find the best certificate for you!
          <br><br>
          <a href="https://blog.pathwaynewsroom.org/2020/10/5-tips-choosing-a-certificate/" style="width: 70px; height: 30px; padding: 20px 10px; border: #f7f7f7 solid; margin: 20px 0; background-color: #f7f7f7;"> Tips for Choosing a certificate </a>
          <br><br>
        </div>

        
        <div style="font-style: italic; border-left: 4px solid #ddd; padding-left: 10px; margin-bottom: 20px;">
            "Eternal life is eternal joy. Joy in this life, right now — not despite challenges of our day but because of the Lord’s help to learn from and ultimately overcome them."
            <br>
            — Sister Amy A. Wright
            <br>
        </div>
        
        <div style="line-height: 1.6; margin: 20px 0;">
            Find what Program is best for you to take this coming semester!
            <br>
            <a href="https://www.byupathway.edu/degrees/program-list" target="_blank">>>Degree List<<</a>
        </div>

        <div style="font-weight: bold;">
           Warm Regards,
            <p>--</p>
            <br>

            <p><strong>Aaron Santos
            <br>
            Mentor</strong></p>

            <span>Whatsapp:</span> (+63) 9532800922
            <br>
            <span>Facebook:</span> <a href="https://www.facebook.com/aaronphil2z.santos/" target="_blank" style="color: blue;">https://www.facebook.com/aaronphil2z.santos/</a>
            <br>
            <span>LinkedIn:</span> <a href="https://www.linkedin.com/in/aaron-santos-a1561b22b/" target="_blank" style="color: blue;">https://www.linkedin.com/in/aaron-santos-a1561b22b/</a>
        </div>
    </div>
</body>
</html>
"""
    
    with open('contacts.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            send_email(row["Name"], row["Email"], subject, body_template)
            print(f"Email sent to {row['Name']} at {row['Email']}")
            time.sleep(3)  
        print("All emails sent")