# -*- coding: utf-8 -*-

# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

def sendip(sendaddr,ipaddr):
    # 以下の内容を変更する
    # me : 自分のGmail アドレス, you : 送信先のアドレス, passwd : Gmailパスワード
    me = "my@email.com"
    passwd = "mypassword"
    you = sendaddr
    titletext = "現在のGlobalIPは"
    body = '[ipaddr]です。'.replace('ipaddr',ipaddr)
    
    msg = MIMEText(body)
    msg['Subject'] = titletext
    msg['From'] = me
    msg['To'] = you
    
    # Send the message via our own SMTP server.
    s = smtplib.SMTP('smtp.gmail.com',587)
    s.ehlo()
    s.starttls()
    s.ehlo()
    s.login(me, passwd)
    s.send_message(msg)
    s.close()
