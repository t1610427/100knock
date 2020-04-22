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
'''
69:一番
70:獰悪（どうあく）が初出
ニャーニャー	名詞,一般,,,,,* -->surfaceで取り出す
'''

long_noun=''                #連接している名詞（文字列）
long_noun_list=[]           #連接している名詞を格納するリスト
long_noun_list.append('')   #[-1]の要素を確認するときのエラー回避のため

for data in result:
    if data['pos']==('名詞'):
        long_noun += data['surface']        #出てきた名詞をstr型でlong_nounに連結。
        if long_noun_list[-1] in long_noun: 
            long_noun_list[-1]=long_noun    #名詞リストの最後がlong_nounに部分一致するなら更新。
        else:
            long_noun_list.append(long_noun)#一致しないならそのまま名詞リストに追加
    else:
        long_noun = ''

#print(long_noun_list[:50])
#print(len(long_noun_list))-->48403

'''
実行結果
['一', '吾輩', '猫', '名前', 'どこ', '見当', '何', '所', 'ニャーニャー', 'いた事', '記憶', '吾輩', 
'ここ', '人間', 'もの', 'あと', 'それ', '書生', '人間中', '一番獰悪', '種族', 'そう', '書生', 'の', 
'我々', '話', '当時', '何', '考', '彼', '掌', 'スー', '時', '感じ', '掌', '上', '書生', '顔', 'の', 
'人間', 'もの', '始', '時妙', 'もの', '感じ', '今', '一毛', '装飾', 'はず', '顔']
'''
#重複除去
long_noun_set=set(long_noun_list)
#print(len(long_noun_set))-->11337