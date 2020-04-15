import re

with open('hightemp.txt',encoding="utf-8_sig") as f:
    f_list=[re.sub(r'\t',' ',i) for i in f.readlines()]  #タブ区切を空白区切に置換

print(f_list)

'''
実行結果
['高知県 江川崎 41 2013-08-12\n',
'埼玉県 熊谷 40.9 2007-08-16\n',
'岐阜県 多治見 40.9 2007-08-16\n',
'山形県 山形 40.8 1933-07-25\n',
'山梨県 甲府 40.7 2013-08-10\n',
'和歌山県 かつらぎ 40.6 1994-08-08\n',
'静岡県 天竜 40.6 1994-08-04\n',
'''

'''
cat hightemp.txt | sed "s/\t/\ /g"
高知県 江川崎 41 2013-08-12
埼玉県 熊谷 40.9 2007-08-16
岐阜県 多治見 40.9 2007-08-16
山形県 山形 40.8 1933-07-25
山梨県 甲府 40.7 2013-08-10
和歌山県 かつらぎ 40.6 1994-08-08
'''

#正規表現reモジュール
#置換後の文字列 = re.sub(正規表現, 置換する文字列, 置換される文字列 [, 置換回数])

#readlines()はファイルの内容を全て読みだし、1行ごとのリストにする。小さいファイルならread()かreadlines()
#ファイルが大きい場合はreadline()で一行ずつ読み込みがO