import smtplib
from smtplib import SMTP 
from email.message import EmailMessage
def sendmail(to,subject,body):
    server=smtplib.SMTP_SSL('smtp.gmail.com',465)
    server.login('aswinimaramreddy2002@gmail.com','cawx hezq xqse enip')
    msg=EmailMessage()
    msg['From']="aswinimaramreddy2002@gmail.com"
    msg['subject']=subject
    msg['To']=to
    msg.set_content(body)
    server.send_message(msg)
    server.quit()