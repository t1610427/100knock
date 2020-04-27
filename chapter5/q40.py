# -*- coding: utf-8 -*-
import CaboCha

c = CaboCha.Parser()
with open('neko.txt')as input_f:
    text = input_f.read()
    tree =  c.parse(text)
    #print(tree.toString(CaboCha.FORMAT_LATTICE))
       
    with open('neko.txt.cabocha', 'w')as output_f:
        output_f.write(tree.toString(CaboCha.FORMAT_LATTICE))

################################################################


class Morph:
    """このクラスは表層形(surface), 基本形(base), 品詞(pos), 品詞細分類1(pos1)をメンバ変数に持つ"""
    #"""...""" で ドキュメントストリング を記述
    def __init__(self, surface, base, pos, pos1): #コンストラクタ
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

    def printMorph(self):
        print(f"surface:{self.surface}, base:{self.base}, pos:{self.pos}, pos1:{self.pos1}")
        
    def __str__(self):
        """__str__() は、インスタンスを暗黙的に文字列に変換する際の変換処理を定義"""
        return f"surface:{self.surface}, base:{self.base}, pos:{self.pos}, pos1:{self.pos1}"
        
        
################################################################

#CaboChaの解析結果（neko.txt.cabocha）を読み込む
with open('neko.txt.cabocha')as f:
    f_list = f.readlines()  #一行ずつ
    f_list = f_list[:-1]    #EOS除去

'''
1行目
* 文節番号 係り先の文節番号(係り先なし:-1) 主辞の形態素番号/機能語の形態素番号 係り関係のスコア(大きい方が係りやすい)
2行目
表層形(Tab区切り)品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
'''
    
    
#各文をMorphオブジェクトのリストとして表現
sentence      = []#Morphオブジェクトが文単位で一時的に入るリスト
sentence_list = []#Morpオブジェクトの文単位のリストが入るリスト(。区切り)
'''
sentence = [どこ, で生まれ,た,か,とんと,見当,が,つか,ぬ,。]
sentence_list.append(sentence)
sentence_list = [[吾輩,は,猫,で,ある,。], [名前,は,まだ,無い,。],[どこ, で生まれ,た,か,とんと,見当,が,つか,ぬ,。]]
'''
    
for line in f_list:
    #print(line,end='')
    if line[0] == '*':
        continue
    else:
        surface  = line.split('\t')[0]
        result_r = line.split('\t')[1]  #\t区切の右側、品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
        pos  = result_r.split(',')[0]
        pos1 = result_r.split(',')[1]
        base = result_r.split(',')[6]
      
        result = Morph(surface, base, pos, pos1)    #クラスのインスタンスを生成
       
        sentence.append(result)                     #sentenceに格納
        if result.surface == '。':
            sentence_list.append(sentence)          #sentence_listに一文分のMorphオブジェクト格納
            sentence = [] 
    
    
#3文目の形態素列を表示せよ．
for i in sentence_list[2]:
    #i.printMorph()#printMorph()メソッドをコール
    print(i)

'''
surface:　, base:　, pos:記号, pos1:空白
surface:どこ, base:どこ, pos:名詞, pos1:代名詞
surface:で, base:で, pos:助詞, pos1:格助詞
surface:生れ, base:生れる, pos:動詞, pos1:自立
surface:た, base:た, pos:助動詞, pos1:*
surface:か, base:か, pos:助詞, pos1:副助詞／並立助詞／終助詞
surface:とんと, base:とんと, pos:副詞, pos1:一般
surface:見当, base:見当, pos:名詞, pos1:サ変接続
surface:が, base:が, pos:助詞, pos1:格助詞
surface:つか, base:つく, pos:動詞, pos1:自立
surface:ぬ, base:ぬ, pos:助動詞, pos1:*
surface:。, base:。, pos:記号, pos1:句点
'''