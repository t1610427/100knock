N = input("input:")

with open('hightemp.txt',encoding="utf-8_sig") as f:
    if N.isnumeric():     #全ての文字が数を表す文字なら真
        for f_line in f.readlines()[-int(N):]:      #末尾からN行をf_lineに
            print(f_line)

'''
実行結果
input:3
山梨県  大月    39.9    1990-07-19
山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02
'''

'''
tail -5 hightemp.txt
埼玉県  鳩山    39.9    1997-07-05
大阪府  豊中    39.9    1994-08-08
山梨県  大月    39.9    1990-07-19
山形県  鶴岡    39.9    1978-08-03
愛知県  名古屋  39.9    1942-08-02
'''