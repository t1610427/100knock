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
###################################################
pos1_list=[]        #サ変接続の名詞のリスト
for i in result:
    if i['pos'] =='名詞':
        if i['pos1']=='サ変接続':
            pos1_list.append(i['surface'])
#print(len(pos1_list))#-->5208
print(pos1_list[:50])

'''
実行結果
['見当', '記憶', '話', '装飾', '突起', '運転', '記憶', '分別', '決心', '我慢', '餓死', '訪問', '始末', '猶予', 
'遭遇', '我慢', '記憶', '返報', '勉強', '勉強', '昼寝', '珍重', '昼寝', '経験', '供', '供', '供', '供', '——', '——', 
'同居', '観察', '断言', '同衾', '供', '迫害', '尊敬', '生活', '剿滅', '議論', '所有', '憤慨', '観念', '御馳走', 
'掠奪', '代言', '我儘', '我儘', '失敗', '話']
'''