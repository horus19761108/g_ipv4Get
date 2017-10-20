# -*- coding: utf-8 -*-

import re
import requests

def getIpv4(siteurl):
    #Webページ情報の取得
    html = getHtml(siteurl)
    if not html:
        ipAddr = 'URL ERROR'
    else:
        #文字コードのセット
        html.encoding = html.apparent_encoding

        #正規表現を利用してIPアドレス(IPv4)であろう文字列を取得
        ipv4_pattan = re.compile(r'(([1-9]?[0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9]{2}|[1-9]?[0-9])')
        search_result = ipv4_pattan.search(html.text)
        if search_result:
            ipAddr = search_result.group()
        else:
            ipAddr = 'Not Global-IPv4-Kakunin-Site'

    return ipAddr
     
def getHtml(url):
    try:
        res = requests.get(url)
    except:
        res = None
    
    return res
