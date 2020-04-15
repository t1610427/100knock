count_line=0        #行数

with open('./hightemp.txt') as f:
    for i in f:
        count_line += 1
print(count_line)

'''
実行結果
24
'''

'''
#wc hightemp.txt
#--> 24  96 813 hightemp.txt
'''

#with文はclose()の呼び出しが不要
