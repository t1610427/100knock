ans=[]

with open('col1.txt') as c1_f, open('col2.txt') as c2_f:        #col1.txtをc1_f,col2.txtをc2_f
    for c1_line, c2_line in zip(c1_f, c2_f):
        ans.append(c1_line.strip("\n") + '\t' + c2_line)        #1列目から'\n'を除いてタブ区切りで2列目を連結

with open('merge.txt', 'w') as f:
    f.write(''.join(ans))

'''
実行結果merge.txt
高知県	江川崎
埼玉県	熊谷
岐阜県	多治見
山形県	山形
山梨県	甲府
和歌山県	かつらぎ
'''

'''
paste col1.txt col2.txt > merge_test.txt                          
高知県	江川崎
埼玉県	熊谷
岐阜県	多治見
山形県	山形
山梨県	甲府
和歌山県	かつらぎ
'''

#zip:複数のリストの要素をまとめて取得
