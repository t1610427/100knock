import MeCab
import sys

dic={}
result=[]
#渡された形態素解析結果を辞書型にして返す
def make_dic(result):
    dic     = {}
    surface = result.split('\t')[0]     #\t区切の左側が表層形
    result_r= result.split('\t')[1]     #\t区切の右側    
    base    = result_r.split(',')[6]    #右側の","区切の6番目が基本形
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
surface_list=[]     #動詞の表層形のリスト

for i in result:
    if i['pos']=='動詞':
        surface_list.append(i['surface'])
#print(len(surface_list))#-->28908
print(surface_list[:50])

'''
実行結果
['生れ', 'つか', 'し', '泣い', 'し', 'いる', '始め', '見', '聞く', '捕え', '煮', '食う', '思わ', 
'載せ', 'られ', '持ち上げ', 'られ', 'し', 'あっ', '落ちつい', '見', '見', '思っ', '残っ', 'いる', 
'さ', 'れ', 'し', '逢っ', '出会わ', 'し', 'なら', 'し', 'いる', '吹く', 'せ', '弱っ', '飲む', 
'知っ', '坐っ', 'おっ', 'する', 'し', '始め', '動く', '動く', '分ら', '廻る', 'なる', '助から']
'''