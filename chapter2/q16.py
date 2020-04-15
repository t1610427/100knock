import math
var = int(input("input:"))
line_count=0

with open('hightemp.txt',encoding="utf-8_sig") as f:
    f_lines = f.readlines()

line_count = len(f_lines)                   #元ファイルの行数の取得
out_f_lines = math.ceil(line_count / var)   #出力ファイル1つの行数
out_f_lines_list = list(range(1,line_count,out_f_lines)) 
#各出力ファイルの元ファイルにおける始まりの行数
#例.input=5-->[1,6,11,16,21]
#P74実例を使う


for i, first in enumerate(out_f_lines_list):
    with open("q16_split{}.txt".format(i),'w') as out_f:        #出力ファイルの名前を決定
        if first + out_f_lines < line_count:                    #先頭行数＋出力ファイルの行数 < 元ファイルの行数
            for line in f_lines[first-1:first-1 + out_f_lines]: #
                out_f.write(line)
        else:                                                   #出力ファイルの行数が足りない時
            for line in f_lines[first-1:line_count]:
                out_f.write(line)
'''
実行結果
q16_split0.txt
高知県	江川崎	41	2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
山梨県	甲府	40.7	2013-08-10

q16_split4.txt
大阪府	豊中	39.9	1994-08-08
山梨県	大月	39.9	1990-07-19
山形県	鶴岡	39.9	1978-08-03
愛知県	名古屋	39.9	1942-08-02
'''

'''
split オプション 元ファイル名 出力ファイルベースファイル名
split -l 5 hightemp.txt q16_test
q16_testa
高知県	江川崎	41	2013-08-12
埼玉県	熊谷	40.9	2007-08-16
岐阜県	多治見	40.9	2007-08-16
山形県	山形	40.8	1933-07-25
山梨県	甲府	40.7	2013-08-10

q16_testb
和歌山県	かつらぎ	40.6	1994-08-08
静岡県	天竜	40.6	1994-08-04
山梨県	勝沼	40.5	2013-08-10
埼玉県	越谷	40.4	2007-08-16
群馬県	館林	40.3	2007-08-16
'''


'''
input=7の時7分割
hightemp.txtは24行のファイルなので
24 / 7 = 3.42...->4
4, 4, 4, 4, 4, 4,行のファイルにする（切り上げ）

'''