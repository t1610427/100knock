class Morph:
    """このクラスは表層形(surface), 基本形(base), 品詞(pos), 品詞細分類1(pos1)をメンバ変数に持つ"""
    #"""...""" で ドキュメントストリング を記述
    def __init__(self, surface, base, pos, pos1): #コンストラクタ
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

    def __str__(self):
        """__str__() は、インスタンスを暗黙的に文字列に変換する際の変換処理を定義"""
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
    
    def pick_surface(self):
        surface_str=''
        for i in self.morphs:
            if i.pos != '記号':
                surface_str += i.surface
        return surface_str
    
    def pick_verb(self):
        for i in self.morphs:
            if i.pos == '動詞':
                return i.base
        return None
    
    def pick_particle(self):
        for i in self.morphs:
            if i.pos == '助詞':
                return i.base
        return None
    
    
    def check_noun(self):
        for i in self.morphs:
            if i.pos == '名詞':
                return True
        return False

    def check_verb(self):
        for i in self.morphs:
            if i.pos == '動詞':
                return True
        return False
    
    def check_particle(self):
        for i in self.morphs:
            if i.pos == '助詞':
                return True
        return False
    
    
def make_morph(file_line):
    surface  = file_line.split('\t')[0]
    result_r = file_line.split('\t')[1]#\t区切の右側、品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音
    
    pos  = result_r.split(',')[0]
    pos1 = result_r.split(',')[1]
    base = result_r.split(',')[6]
      
    morph_e = Morph(surface, base, pos, pos1)#クラスのインスタンスを生成
    return morph_e
    
def make_chunk(chunk_elemnt):
    morphs = chunk_elemnt[0]
    dst    = chunk_elemnt[1]
    srcs   = chunk_elemnt[2]
    chunk_e= Chunk(morphs, dst, srcs)
    return chunk_e
    
def make_chunk_list(morph_element, chunk_element):
    chunk_element.insert(0,morph_element)#先頭にmorphオブジェクトを追加
    chunk_=make_chunk(chunk_element)
    chunk_list.append(chunk_)#chunkリストに追加
    return chunk_list


def pick_dstElem_from_dstNum(sentence_l, dst_num):
    for s_l in sentence_l:
        for chunk_e in s_l:
            if chunk_e.srcs == dst_num:
                return chunk_e
    return None

def pick_srcsElem_from_srcsNum(sentence_l, srcs_num):
    srcs_elements = []
    for chunk_e in sentence_l:
        if chunk_e.dst == srcs_num:
            srcs_elements.append(chunk_e)
    return srcs_elements

    
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
chunk_elem = [morph_elem, 1D,0]
chunk_list = [chunk_elem1, chunk_elem1]
sentence_list = [chunk_list1, chunk_list2]
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

            
            
srcs_str=''#係り元文節の文字列
dst_str =''#係り先文節の文字列
ans = '' #'述語\t格のリスト'の文字列
ans_list = []

#10文分
for s_l in sentence_list[:10]:
    for chunk_e in s_l:
        srcs_num = (chunk_e.srcs)
        dst_num  = (chunk_e.dst)
     
        if chunk_e.check_verb():
            dst_str = chunk_e.pick_verb()
          
            srcs_elems = pick_srcsElem_from_srcsNum(s_l, srcs_num)#その文節にかかる文節のリスト
            
            if srcs_elems != []:
                particle_l=[]
                srcs_surface_l =[]#46係り元の表層形のリスト
                
                for srcs_elem in srcs_elems:                    
                    if srcs_elem.check_particle():      #係り元文節に助詞があるときTrue
                        srcs_surface_l.append(srcs_elem.pick_surface())#
                        particle_l.append(srcs_elem.pick_particle())
            
                srcs_str = ' '.join(i for i in particle_l)
                ans = dst_str + '\t' + srcs_str + '\t' + ' '.join(i for i in srcs_surface_l)
           
                ans_list.append(ans)

'''
for i in ans_list[:20]:
    print(i)
 
生れる	で	どこで
つく	か が	生れたか 見当が
泣く	で	所で
する	て だけ	泣いて いた事だけは
始める	で	ここで
見る	は を	吾輩は ものを
聞く	で	あとで
捕える	を	我々を
煮る	て	捕えて
食う	て	煮て
思う	から	なかったから
載せる	に	掌に
持ち上げる	て と	載せられて スーと
する		
ある	が	感じが
落ちつく	で	上で
見る	て を	落ちついて 顔を
見る	の	ものの
'''