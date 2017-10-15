# 概要
* python3練習用スクリプト
    * グローバルIPを取得するためのスクリプト
    * グローバルIP確認用サイト(確認くんみたいなサイト)を利用する。
    * サイトは複数登録できるものとする。
    * OS上でタスク化し取得したIPアドレスを、メールでお知らせ

# 開発環境
* OS
    * Windows10(1703) Home
* 開発言語
    * Python 3.6
    
# 開発履歴
[2017/10/15]
* mailtool.py
    * 関数[ipsend(mailaddr,bodytext)]
        * 引数mailaddr宛にbodytextをgmail経由でメールする。
[2017/10/14]
* webtool.py
    * 関数[getHtml(url)]
        * 引数urlから、webページのhtmlを取得しrequests.models.Responseオブジェクトを返す(requests利用)。  
          エラーの場合はNoneを返す。
    * 関数[getIpv4(siteurl)]
        * 引数siteurlから、関数[getHtml]で取得したwebページからIPアドレスと思われる部分をStr型で返す  
          引数siteurlのWebページへアクセスできない場合は'URL ERROR'を返す  
          引数siteurlのWebページからIPアドレスが取得できない場合は'Not Global-IPv4-Kakunin-Site'を返す
* fileaccess.py
    * 関数[read_file()]
        * Tkinterを使って、ファイルダイアログよりテキストファイルの中身を、リスト型で返す
    * 関数[file_view()]
        * 関数[read_file()]テスト用。
        * 読み込んだファイルの中身をコンソールへ表示する。
