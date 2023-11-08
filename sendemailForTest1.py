from email.mime.text import MIMEText
import smtplib
from email.mime.multipart import MIMEMultipart

def sendingmail(mail_content,email):
    msg = MIMEMultipart()
    
    password = "skvm@123"
    msg['From'] = "skvmtravels@gmail.com"

    server = smtplib.SMTP('smtp.gmail.com: 587')
    
    server.starttls()
    
    server.login(msg['From'], password)

    msg['To'] = email
    msg['Subject'] = "Info regarding your council details"

        # the message to be emailed
        
    msg.attach(MIMEText(mail_content, 'plain'))
    
    server.sendmail(msg['From'], msg['To'], msg.as_string())

    
    server.quit()
    
    print("successfully sent email to %s" % (msg['To']))
