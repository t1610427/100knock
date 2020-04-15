col1=[]
i=0

with open('hightemp.txt',encoding="utf-8_sig") as f:
    f_list=f.readlines()
    for i in range(len(f_list)):
        col1.append(f_list[i].split("\t")[0])       #タブ区切の0番目をcol1に
    col1_set=set(col1)                              #集合にする

print(col1_set)

'''
実行結果
{'愛知県', '岐阜県', '愛媛県', '大阪府', '千葉県', '和歌山県', '群馬県', '山梨県', '静岡県', '高知県', '埼玉県', '山形県'}
'''

'''
 cat ./hightemp.txt | cut -f1 | sort | uniq
愛知県
愛媛県
岐阜県
群馬県
高知県
埼玉県
山形県
山梨県
静岡県
千葉県
大阪府
和歌山県
'''