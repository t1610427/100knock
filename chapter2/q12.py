f_list=[]
col1=[]     #各ファイルの1列目を格納するリスト
col2=[]     #各ファイルの2列目を格納するリスト
i=0

with open('./hightemp.txt',encoding="utf-8_sig") as f:
    for f_list in f.readlines():
        col1.append(f_list.split()[0]+"\n")  #空白区切の0番目(県名)の列をco1に
        col2.append(f_list.split()[1]+"\n")  #空白区切の1番目(市名)の列をco2に

with open('col1.txt', 'w') as f1:
    f1.write(''.join(col1))

with open('col2.txt', 'w') as f2:
    f2.write(''.join(col2))

'''
実行結果col1.txt
高知県
埼玉県
岐阜県
山形県
山梨県
和歌山県
'''

'''
実行結果col2.txt
江川崎
熊谷
多治見
山形
甲府
かつらぎ
'''

'''
cut -f 1 hightemp.txt > col1_test.txt
cut -f 2 hightemp.txt > col2_test.txt
col1_test.txt
高知県
埼玉県
岐阜県
山形県
山梨県
和歌山県
'''