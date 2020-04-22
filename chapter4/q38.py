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
            
#与えられた辞書と辞書の値から、辞書のキーを取得する関数
def get_keys_from_value(dic, val):
    return [k for k, v in dic.items() if v == val]


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

c2 = collections.Counter(base_list2)    #出現頻度を取得
count_list = list(c2.values())          #出現頻度のみのリストを作成
count_list.sort()                       #昇順に並び替え
#count_list.sort(reverse=True)#降順

'''
出現回数
1回が4718個
2回が1905個
'''

plt.rcParams["font.family"] = "IPAexGothic"
plt.title('出現頻度ヒストグラム')
plt.hist(count_list, bins=100, range=(0, 50))
plt.savefig('q38ans.png')

plt.rcParams["font.family"] = "IPAexGothic"
plt.title('出現頻度ヒストグラム')
plt.hist(count_list, bins=100, range=(50, 100),color="red")
plt.savefig('q38ans2.png')

'''
#binsビン(表示する棒)の数.デフォ10
#rangeビンの最小値と最大値を指定。(デフォルト値: (x.min(), x.max())) 
'''