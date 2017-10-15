# -*- coding:utf-8 -*-

import webtool,mailtool

filename = "urllists.txt"
with open (filename, 'r', encoding='utf8') as input:
    data = input.read()
    data = data.split("\n")
    
for i in data:
    ipaddr = webtool.getIpv4(i)
    if ipaddr:
        break

if ipaddr:
    sendaddr = 'rcpt@email'
    try:
        mailtool.sendip(sendaddr,ipaddr)
    except:
        print('Don\'t send to mail...')
