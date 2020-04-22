# coding:utf-8
import MeCab
import sys
import pprint

with open("neko.txt") as f:
    text = f.read()
    with open('neko.txt.mecab','w') as f:
        m = MeCab.Tagger()
        f.write(m.parse(text))      #解析結果をneko.txt.mecabに保存
'''
解析結果は下の形
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用型,活用形,原形,読み,発音
'''
dic={}
result=[]

#渡された形態素解析結果を辞書型にして返す
#P47縦の線を真っすぐにする
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
#print(len(result)) #-->206392
pprint.pprint(result[:50])

'''
ans[:50]までの出力結果
[{'base': '一', 'pos': '名詞', 'pos1': '数', 'surface': '一'},
 {'base': '\u3000', 'pos': '記号', 'pos1': '空白', 'surface': '\u3000'},
 {'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞', 'surface': '吾輩'},
 {'base': 'は', 'pos': '助詞', 'pos1': '係助詞', 'surface': 'は'},
 {'base': '猫', 'pos': '名詞', 'pos1': '一般', 'surface': '猫'},
 {'base': 'だ', 'pos': '助動詞', 'pos1': '*', 'surface': 'で'},
 {'base': 'ある', 'pos': '助動詞', 'pos1': '*', 'surface': 'ある'},
 {'base': '。', 'pos': '記号', 'pos1': '句点', 'surface': '。'},
 {'base': '名前', 'pos': '名詞', 'pos1': '一般', 'surface': '名前'},
 {'base': 'は', 'pos': '助詞', 'pos1': '係助詞', 'surface': 'は'},
 {'base': 'まだ', 'pos': '副詞', 'pos1': '助詞類接続', 'surface': 'まだ'},
 {'base': '無い', 'pos': '形容詞', 'pos1': '自立', 'surface': '無い'},
 {'base': '。', 'pos': '記号', 'pos1': '句点', 'surface': '。'},
 {'base': '\u3000', 'pos': '記号', 'pos1': '空白', 'surface': '\u3000'},
 {'base': 'どこ', 'pos': '名詞', 'pos1': '代名詞', 'surface': 'どこ'},
 {'base': 'で', 'pos': '助詞', 'pos1': '格助詞', 'surface': 'で'},
 {'base': '生れる', 'pos': '動詞', 'pos1': '自立', 'surface': '生れ'},
 {'base': 'た', 'pos': '助動詞', 'pos1': '*', 'surface': 'た'},
 {'base': 'か', 'pos': '助詞', 'pos1': '副助詞／並立助詞／終助詞', 'surface': 'か'},
 {'base': 'とんと', 'pos': '副詞', 'pos1': '一般', 'surface': 'とんと'},
 {'base': '見当', 'pos': '名詞', 'pos1': 'サ変接続', 'surface': '見当'},
 {'base': 'が', 'pos': '助詞', 'pos1': '格助詞', 'surface': 'が'},
 {'base': 'つく', 'pos': '動詞', 'pos1': '自立', 'surface': 'つか'},
 {'base': 'ぬ', 'pos': '助動詞', 'pos1': '*', 'surface': 'ぬ'},
 {'base': '。', 'pos': '記号', 'pos1': '句点', 'surface': '。'},
 {'base': '何', 'pos': '名詞', 'pos1': '代名詞', 'surface': '何'},
 {'base': 'でも', 'pos': '助詞', 'pos1': '副助詞', 'surface': 'でも'},
 {'base': '薄暗い', 'pos': '形容詞', 'pos1': '自立', 'surface': '薄暗い'},
 {'base': 'じめじめ', 'pos': '副詞', 'pos1': '一般', 'surface': 'じめじめ'},
 {'base': 'する', 'pos': '動詞', 'pos1': '自立', 'surface': 'し'},
 {'base': 'た', 'pos': '助動詞', 'pos1': '*', 'surface': 'た'},
 {'base': '所', 'pos': '名詞', 'pos1': '非自立', 'surface': '所'},
 {'base': 'で', 'pos': '助詞', 'pos1': '格助詞', 'surface': 'で'},
 {'base': '*\n', 'pos': '名詞', 'pos1': '一般', 'surface': 'ニャーニャー'},
 {'base': '泣く', 'pos': '動詞', 'pos1': '自立', 'surface': '泣い'},
 {'base': 'て', 'pos': '助詞', 'pos1': '接続助詞', 'surface': 'て'},
 {'base': 'いた事', 'pos': '名詞', 'pos1': '一般', 'surface': 'いた事'},
 {'base': 'だけ', 'pos': '助詞', 'pos1': '副助詞', 'surface': 'だけ'},
 {'base': 'は', 'pos': '助詞', 'pos1': '係助詞', 'surface': 'は'},
 {'base': '記憶', 'pos': '名詞', 'pos1': 'サ変接続', 'surface': '記憶'},
 {'base': 'する', 'pos': '動詞', 'pos1': '自立', 'surface': 'し'},
 {'base': 'て', 'pos': '助詞', 'pos1': '接続助詞', 'surface': 'て'},
 {'base': 'いる', 'pos': '動詞', 'pos1': '非自立', 'surface': 'いる'},
 {'base': '。', 'pos': '記号', 'pos1': '句点', 'surface': '。'},
 {'base': '吾輩', 'pos': '名詞', 'pos1': '代名詞', 'surface': '吾輩'},
 {'base': 'は', 'pos': '助詞', 'pos1': '係助詞', 'surface': 'は'},
 {'base': 'ここ', 'pos': '名詞', 'pos1': '代名詞', 'surface': 'ここ'},
 {'base': 'で', 'pos': '助詞', 'pos1': '格助詞', 'surface': 'で'},
 {'base': '始める', 'pos': '動詞', 'pos1': '自立', 'surface': '始め'},
 {'base': 'て', 'pos': '助詞', 'pos1': '接続助詞', 'surface': 'て'}]
'''