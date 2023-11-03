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
    subject = "What can I pray for on your behalf?"
    body_template = """
<html>
<head>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 20px; color: #333;">
    <div style="max-width: 600px; background-color: #fff; padding: 20px; border-radius: 8px; margin: auto;">
        <div style="font-size: 20px; font-weight: bold; margin-bottom: 15px;">Good day {name}!</div>
        
        <div style="line-height: 1.6; margin-bottom: 20px;">
           Congratulations! You are halfway through the semester! I hope you are feeling more confident with the coursework and enjoy what you are learning. As your Mentor, part of my role is to help you stay motivated to continue your studies successfully.
        </div>
        
        <div style="line-height: 1.6; margin-bottom: 20px;">
           If you are feeling a little overwhelmed, I invite you to consider King Benjamin’s advice:
           <br>
           “And see that all these things are done in wisdom and order; for it is not requisite that a man should run faster than he has strength. And again, it is expedient that he should be diligent, that thereby he might win the prize; therefore, all things must be done in order.” Mosiah 4:27
        </div>

        <div style="line-height: 1.6; margin-bottom: 20px;">
            Here are two principles that can help you use “wisdom and order”:
            <ol>
                <li>Remember your "WHY":  Post or hang a picture that helps you remember and feel excited about why you are doing BYU-Pathway.</li>

                <li>Counsel with the Lord through prayer. The Lord knows everything you are experiencing! As you rely on Him, He can show you the way to accomplish what He is asking you to do (1 Nephi 3:7).</li>
            </ol>
             Whatever challenge you may be facing, please know that I am here to support your efforts. What can I pray for on your behalf?
        </div>   


        <div style="line-height: 1.6; margin-bottom: 20px;">
          <b>Succeed With Smart Goals!</b> <br>
          Start the term off right by creating some new SMART goals! Simply follow the steps below, regularly evaluate how things are going, and adjust if necessary.
          <img src="https://mktdplp102wuda.azureedge.net/org-e59284a505b84d27bcc99cfe9ec003e9/07b310af-8a15-ec11-b6e6-000d3a3002e5/41kGBDO57KypFYBJt_D6ac8oZShEu18Y65joCOTM4tw!" alt="smart goals" style="width: 100%;">
        </div>

        
        <div style="font-style: italic; border-left: 4px solid #ddd; padding-left: 10px; margin-bottom: 20px;">
            "Eternal life is eternal joy. Joy in this life, right now — not despite challenges of our day but because of the Lord’s help to learn from and ultimately overcome them."
            <br>
            — Sister Amy A. Wright
            <br>
        </div>
        
        <div style="line-height: 1.6; margin: 20px 0;">
            Did you know that BYU-Pathway has tutoring services?
            <br>
            <a href="https://www.byui.edu/tutoring-center/online-tutoring" target="_blank">Click Here to Find A Tutor</a>
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