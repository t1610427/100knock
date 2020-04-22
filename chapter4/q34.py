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
#初出、116-118に"彼の掌"
a_b=[]      #二つの名詞が「の」で連結されている名詞句のリスト

#for文でi番目の要素が名詞かつ、i+1番目が'の'かつi+2番目が名詞を探す
for i, dic in enumerate(result):
    if i > len(result)-3:
        break               #最後要素2個のときIndexErrorになるから

    dic_next  = result[i+1]   #i+1番目
    dic_next2 = result[i+2]   #i+2番目

    if dic['pos']=='名詞' and dic_next['surface']=='の' and dic_next2['pos']=='名詞':
        '''動作確認用
        print(dic['surface'],end='')
        print(dic_next['surface'],end='')
        print(dic_next2['surface'])
        '''
        a_b.append(dic['surface']+dic_next['surface']+dic_next2['surface'])

print(a_b[:50])

'''
実行結果
['彼の掌', '掌の上', '書生の顔', 'はずの顔', '顔の真中', '穴の中', '書生の掌', '掌の裏', '何の事', 
'肝心の母親', '藁の上', '笹原の中', '池の前', '池の上', '一樹の蔭', '垣根の穴', '隣家の三', '時の通路', 
'一刻の猶予', '家の内', '彼の書生', '以外の人間', '前の書生', 'おさんの隙', 'おさんの三', '胸の痞', 
'家の主人', '主人の方', '鼻の下', '吾輩の顔', '自分の住', '吾輩の主人', '家のもの', 'うちのもの', 
'彼の書斎', '本の上', '皮膚の色', '本の上', '彼の毎夜', '以外のもの', '主人の傍', '彼の膝', '膝の上', 
'経験の上', '飯櫃の上', '炬燵の上', 'ここのうち', '供の寝床', '彼等の中間', '供の一']
'''