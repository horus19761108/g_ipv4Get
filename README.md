# 概要
* python3練習用スクリプト
    * グローバルIPを取得するためのスクリプト
    * グローバルIP確認用サイト(確認くんみたいなサイト)を利用する。
    * サイトは複数登録できるものとする。
    * 取得したIPアドレスを、メールでお知らせ
    * OSでタスク化すれば自動化もできる(変更されたかのチェックは後日追加する)

# 開発環境
* OS
    * Windows10(1703) Home
* 開発言語
    * Python 3.6

# 必要なもの
* Gmailアカウント
* URLが記載されたファイル

# URLが記載されたファイルについて
* テキスト形式で作成してください
* グローバルIPが確認できるサイトのURLを1行ずつ記載してください
    * 参考)
      ip_kakunin_url.txt

# 開発履歴
[2017/10/15]
* mailtool.py
    * 関数[def sendip(sendaddr,ipaddr)]
        * 引数sendaddr宛に引数ipaddrを本文へ編集し、gmail経由でメールする。
* getGlobalIPv4_run.py
    * 実行用スクリプト
        * URLが記載されたファイル(ファイルパスはオウンコーディング)を読み込む
        * ファイル内に記載された順にURLへアクセスし、Webページを取得する
        * IPアドレスらしきものを見つけたら、Webページの取得は終了
        * 指定した宛先へ、IPアドレスを記載したメールを送付  
        
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

