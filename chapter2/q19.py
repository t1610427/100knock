import collections

col1_count=[]
col1=[]
with open('hightemp.txt',encoding="utf-8_sig") as f:
    for f_line in f:
        col1.append(f_line.split("\t")[0])  #タブ区切の0番目をcol1に
    col1_count=collections.Counter(col1)    #collections.Counterで出現頻度、counterは辞書型
print(col1_count)

'''実行結果
Counter({'埼玉県': 3, '山形県': 3, '山梨県': 3, '群馬県': 3, '岐阜県': 2, '静岡県': 2, '愛知県': 2, 
'千葉県': 2, '高知県': 1, '和歌山県': 1, '愛媛県': 1, '大阪府': 1})
'''

'''
cat ./hightemp.txt | cut -f1 | sort | uniq -c | sort -rk1
3 山梨県
3 山形県
3 埼玉県
3 群馬県
2 千葉県
2 静岡県
2 岐阜県
2 愛知県
1 和歌山県
1 大阪府
1 高知県
1 愛媛県
'''
