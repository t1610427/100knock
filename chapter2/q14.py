N = input("input:")
count=0

with open('hightemp.txt',encoding="utf-8_sig") as f:
    for f_line in f:
        if N.isnumeric():     #全ての文字が数を表す文字なら真
            count += 1
            if count <= int(N):
                print(f_line)

'''
実行結果
input:3
高知県  江川崎  41      2013-08-12
埼玉県  熊谷    40.9    2007-08-16
岐阜県  多治見  40.9    2007-08-16

input:a
'''

'''
head -3 hightemp.txt
高知県  江川崎  41      2013-08-12
埼玉県  熊谷    40.9    2007-08-16
岐阜県  多治見  40.9    2007-08-16
'''

#input() は引数に標準出力時に表示する文字列を渡す
#input('文字列')