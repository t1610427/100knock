class Morph:
    def __init__(self, surface, base, pos, pos1): 
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

    def __str__(self):
        return f"surface:{self.surface}, base:{self.base}, pos:{self.pos}, pos1:{self.pos1}"
        

class Chunk:
    """このクラスは形態素(Morphオブジェクト)のリスト(morphs),
    係り先文節インデックス番号(dst),
    係り元文節インデックス番号のリスト(srcs),
    をメンバ変数に持つ"""
    def __init__(self, morphs, dst, srcs): #コンストラクタ
        self.morphs = morphs
        self.dst    = dst.split('D')[0]
        self.srcs   = srcs
    
    def __str__(self):
        return "morphs:[{}], srcs:{}, dst:{}".format(''.join([morph.surface for morph in self.morphs]),self.srcs, self.dst)


#与えられた解析結果の一行をmorphクラスに
def make_morph(file_line):
    surface  = file_line.split('\t')[0]
    result_r = file_line.split('\t')[1]
    
    pos  = result_r.split(',')[0]
    pos1 = result_r.split(',')[1]
    base = result_r.split(',')[6]
      
    morph_e = Morph(surface, base, pos, pos1)#morphクラスのインスタンスを生成
    return morph_e
    
#与えられた[morphs, dst, srcs]からchunkオブジェクトを生成
def make_chunk(chunk_elemnt):
    morphs = chunk_elemnt[0]
    dst    = chunk_elemnt[1]
    srcs   = chunk_elemnt[2]
    chunk_e= Chunk(morphs, dst, srcs)#インスタンスを生成
    return chunk_e

def make_chunk_list(morph_element, chunk_element):
    chunk_element.insert(0,morph_element)#先頭にmorphオブジェクトを追加
    chunk_=make_chunk(chunk_element)
    chunk_list.append(chunk_)#chunkリストに追加
    return chunk_list
#####################################################################    
'''
1行目
* 文節番号 係り先の文節番号(係り先なし:-1) 主辞の形態素番号/機能語の形態素番号 係り関係のスコア(大きい方が係りやすい)
2行目
表層形(Tab区切り)品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
'''

#CaboChaの解析結果（neko.txt.cabocha）を読み込む
with open('neko.txt.cabocha')as f:
    f_list = f.readlines()#一行ずつ
    f_list = f_list[:-1]#EOS除去

morph_elem = [] 
chunk_elem = []
chunk_list = []
sentence_list = []
'''
morph_elem = [-, ,吾輩,は]
chunk_elem = [[-, ,吾輩,は],1D,0]-->chunk_
chunk_list = [chunk_1, chunk_2]
sentence_list = [[chunk_1, chunk_2], [chunk_1, chunk_2, chunk_3]]
'''

for line in f_list:
    if line[0] == '*':
        if chunk_elem != []:#係り先文節番号、係り元文節番号が入っている
            chunk_list=make_chunk_list(morph_elem, chunk_elem)
            morph_elem = []
            chunk_elem = []
            
        chunk_elem.append(line.split()[2])
        chunk_elem.append(line.split()[1])

    else:
        result = make_morph(line)
       
        if result.surface != '。':
            morph_elem.append(result)#句点が来るまでインスタンスをmorph_elemに格納
        else:
            morph_elem.append(result)#句点を格納
            sentence_list.append(make_chunk_list(morph_elem, chunk_elem))
            morph_elem = []
            chunk_elem = []
            chunk_list = []

for i in sentence_list[7]:
    print(i)
    
'''
morphs:[しかし], srcs:41, dst:50
morphs:[その], srcs:42, dst:43
morphs:[当時は], srcs:43, dst:46
morphs:[何という], srcs:44, dst:45
morphs:[考も], srcs:45, dst:46
morphs:[なかったから], srcs:46, dst:50
morphs:[別段], srcs:47, dst:48
morphs:[恐し], srcs:48, dst:50
morphs:[いとも], srcs:49, dst:50
morphs:[思わなかった。], srcs:50, dst:61
'''