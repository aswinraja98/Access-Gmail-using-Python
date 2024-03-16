#Libraries
import  smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

#Username and Passwords
username = "<your_mail>"
password = "Your_protected_password"
def send_mail(text ='Email Body',Subject= 'Register your complaints',from_email = 'Hades <ashhades407@gmail.com>',to_emails= None,html = None):
    assert isinstance(to_emails,list)
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ",".join(to_emails)
    msg['Subject'] = Subject

    txt_part = MIMEText(text,'plain')
    msg.attach(txt_part)

    if html is not None:
        html_part = MIMEText("<h1> This is working </h1>",'html')
        msg.attach(html_part)
    msg_str=msg.as_string()


   #Server login
    server = smtplib.SMTP(host = 'smtp.gmail.com',port = 587)
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(from_email,to_emails,msg_str)
    server.quit()


