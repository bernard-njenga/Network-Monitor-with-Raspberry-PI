import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

email_user = 'bnnjenga@zohomail.com'
email_password = 'Menengai21'
email_send = 'bnnjenga@telkom.co.ke'

subject = 'Network Availability User Stats - Rpi_1'

msg = MIMEMultipart()
msg['From'] = email_user
msg['To'] = email_send
msg['Subject'] = subject

body = 'Hello, please find attached network stats till date.'
msg.attach(MIMEText(body,'plain'))

filename='/home/pi/speedtest/speedtestrpi_1.csv'
attachment  =open(filename,'rb')

part = MIMEBase('application','octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition',"attachment; filename= "+filename)

msg.attach(part)
text = msg.as_string()
server = smtplib.SMTP('smtp.zoho.com',587)
server.starttls()
server.login(email_user,email_password)


server.sendmail(email_user,email_send,text)
server.quit()
