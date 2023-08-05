import smtplib
import email.message
import time

msg = email.message.EmailMessage()
def send(master, slave, title, content, smtp, tcp, password):
    msg["From"] = master
    msg["To"] = slave
    msg["Subject"] = title
    msg_time = time.strftime("%m/%d/%Y %H:%M:%S", time.localtime())
    msg.set_content("{}, {}".format(content, msg_time))
    
    server = smtplib.SMTP_SSL(smtp, tcp)
    server.login(master, password)
    server.send_message(msg)
    server.close()