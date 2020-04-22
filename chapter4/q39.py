# coding:utf-8
import MeCab
import sys
import collections
import re
import numpy as np
import matplotlib.pyplot as plt
#import japanize_matplotlib
#from matplotlib.font_manager import FontProperties as fm

dic={}
result=[]
#渡された形態素解析結果を辞書型にして返す
def make_dic(result):
    dic     = {}
    surface = result.split('\t')[0]     #\t区切の左側が表層形
    result_r= result.split('\t')[1]     #\t区切の右側    
    base    = result_r.split(',')[6]    #右側の","区切の7番目が基本形
    pos     = result_r.split(',')[0]    #右側の","区切の0番目が品詞
    pos1    = result_r.split(',')[1]    #右側の","区切の1番目が品詞分類1
    
    dic['surface'] = surface
    dic['base']    = base
    dic['pos']     = pos
    dic['pos1']    = pos1
    return dic

with open("neko.txt.mecab") as f:
    f_list = f.readlines()      #1行区切りでリスト化
    f_list = f_list[:-1]        #末尾のEOS除去
    for f_line in f_list:
        result.append(make_dic(f_line))

'''
解析結果は下の形
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
surface:表層形
base:原形
pos:品詞
pos1:品詞分類1
#ここまではq30.py
'''
###################################################
base_list =[i['base'] for i in result]  #基本形のリスト

base_list2=[]                           #基本形から。,などを除いた基本形リスト
for i in base_list:
    m=re.search("(\w+)",i)
    if m != None:
        base_list2.append(m.group(1))
#################################################
c2 = collections.Counter(base_list2)    #P23スコープ（その名前が見えるコードの行数）が小さいなら短くていい
count_list = list(c2.values())
count_list.sort(reverse=True)#降順
count_rank=list(range(1,len(count_list)+1))
'''
print(len(count_list))#-->11238
print(list(range(1,11238)))#-->1から11238まで
'''

'''
横軸：出現頻度順位
縦軸：出現頻度
'''

plt.rcParams["font.family"] = "IPAexGothic"
plt.title('q39')
plt.xlabel("出現頻度順位")
plt.ylabel("出現頻度")
plt.xscale("log")
plt.yscale("log")
plt.plot(count_list, count_rank)
plt.savefig('q39ans.png')

'''
zipfの法則:出現頻度が k 番目に大きい要素が全体に占める割合が 1 / k に比例するという経験則
冪関数に従う実験データから回帰分析で定数a 、n を求めるとき、冪関数のままだと非線形回帰となるが、
対数をとることで線形回帰として扱うことができ、解析が非常に簡単になる。 
'''