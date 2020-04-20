# coding:utf-8
import re

fname = "uk_text.txt"

with open(fname,'r',encoding="utf-8_sig") as f:
    for f_line in f:        
        media_file_name = re.search(r"\[\[(ファイル|File):(.*?)\|.*\]\]$",f_line) 
        #非貪欲(non-greedy), 最小(minimal)マッチ。でないとRoyal Coat of Arms of the United Kingdom.svg|85pxでうまくいかない
        
        if media_file_name != None:
            print(media_file_name.group(2))

'''
実行結果
Royal Coat of Arms of the United Kingdom.svg
Battle of Waterloo 1815.PNG
The British Empire.png
Uk topo en.jpg
BenNevis2005.jpg
Elizabeth II greets NASA GSFC employees, May 8, 2007 edit.jpg
Palace of Westminster, London - Feb 2007.jpg
David Cameron and Barack Obama at the G20 Summit in Toronto.jpg
Soldiers Trooping the Colour, 16th June 2007.jpg
Scotland Parliament Holyrood.jpg
London.bankofengland.arp.jpg
City of London skyline from London City Hall - Oct 2008.jpg
Oil platform in the North SeaPros.jpg
Eurostar at St Pancras Jan 2008.jpg
Heathrow T5.jpg
Anglospeak.svg
CHANDOS3.jpg
The Fabs.JPG
Wembley Stadium, illuminated.jpg
'''
            
'''
大まかに
XX[[ファイル:XXX.xxx|XX]]
[[File:XXXXXX.xxx|XX]]
の二通り

.
(ドット)デフォルトのモードでは改行以外の任意の文字にマッチ

*
直前の正規表現を 0 回以上、できるだけ多く繰り返したものにマッチ

?
直前の正規表現を 0 回か 1 回繰り返したものにマッチ

.*?
修飾子の後に?に'?'を追加すると非貪欲あるいは最小のマッチが行われ、できるだけ少ない文字にマッチ
############################################################################
例
<.*>が"<a> b <c>"に対してマッチされると"<a>"だけでなく文字列全体にマッチしてしまう
正規表現<.*?>を使うと"<a>"だけにマッチ
############################################################################
$
文字列の末尾、あるいは文字列の末尾の改行の直前にマッチ
'''