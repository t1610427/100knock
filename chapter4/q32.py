import MeCab
import sys

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
##########################################
base_list=[]        #動詞の原形のリスト
for i in result:
    if i['pos']=='動詞':
        base_list.append(i['base'])
#print(len(base_list))#-->28908
print(base_list[:50])

'''
実行結果
['生れる', 'つく', 'する', '泣く', 'する', 'いる', '始める', '見る', '聞く', '捕える', '煮る', '食う', '思う', 
'載せる', 'られる', '持ち上げる', 'られる', 'する', 'ある', '落ちつく', '見る', '見る', '思う', '残る', 'いる', 
'する', 'れる', 'する', '逢う', '出会う', 'する', 'なる', 'する', 'いる', '吹く', 'する', '弱る', '飲む', 
'知る', '坐る', 'おる', 'する', 'する', '始める', '動く', '動く', '分る', '廻る', 'なる', '助かる']
'''