# coding:utf-8
import re

fname = "uk_text.txt"

with open(fname,'r',encoding="utf-8_sig") as f:
    for f_line in f:
        section_line = re.search(r"^(?P<section_level>=+)(?P<section_name>\w+)",f_line)
        #=の1回以上繰り返しをsection_level, その後の単語文字1回以上繰り返しをsection_nameでアクセス可
        if section_line != None:
            s_level = section_line.group('section_level').count('=')-1
            s_name  = section_line.group('section_name')
            print(f"level:{s_level}, name:{s_name}")

'''
実行結果
level:1, name:国名
level:1, name:歴史
level:1, name:地理
level:2, name:気候
level:1, name:政治
level:1, name:外交と軍事
level:1, name:地方行政区分
level:2, name:主要都市
level:1, name:科学技術
level:1, name:経済
level:2, name:鉱業
level:2, name:農業
level:2, name:貿易
level:2, name:通貨
level:2, name:企業
level:1, name:交通
level:2, name:道路
level:2, name:鉄道
level:2, name:海運
level:2, name:航空
level:1, name:通信
level:1, name:国民
level:2, name:言語
level:2, name:宗教
level:2, name:教育
level:1, name:文化
level:2, name:食文化
level:2, name:文学
level:2, name:音楽
level:3, name:イギリスのポピュラー音楽
level:2, name:映画
level:2, name:コメディ
level:2, name:国花
level:2, name:世界遺産
level:2, name:祝祭日
level:1, name:スポーツ
level:2, name:サッカー
level:2, name:競馬
level:2, name:モータースポーツ
level:1, name:脚注
level:1, name:関連項目
level:1, name:外部リンク
'''


'''
==文化== レベル1
===音楽=== レベル2
====イギリスのポピュラー音楽==== レベル3
'='の数-1がレベル数

(?P<name>...)
このグループがマッチした部分文字列はシンボリックグループ名nameでアクセスできる
(?P<quote>['\"]).*?(?P=quote)
m.group('quote')
'''