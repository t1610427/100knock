class Morph:
    def __init__(self, surface, base, pos, pos1): #コンストラクタ
        self.surface = surface
        self.base    = base
        self.pos     = pos
        self.pos1    = pos1

    def __str__(self):
        return f"surface:{self.surface}, base:{self.base}, pos:{self.pos}, pos1:{self.pos1}"
        

class Chunk:
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
    
    def pick_noun(self):
        for i in self.morphs:
            if i.pos == '名詞':
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
    
    def check_particle_wo(self):
        for i in self.morphs:
            if i.pos == '助詞':
                if i.base == 'を':
                    return True
        return False
    
    def check_sa(self):
        for i in self.morphs:
            if i.pos1 == 'サ変接続':
                return True
        return False
    
    ####################################
    def check_root(self):
        for i in self.morphs:
            if i.surface == '。':
                return True
        return False
     ####################################
    
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

##############################################################
#係り先番号の文節が根でないなら再帰的に呼び出される

def make_root_path(sentence_l, dst_num):
    dst_elem = pick_dstElem_from_dstNum(sentence_l, dst_num)
    if dst_elem.check_root():
        return dst_elem.pick_surface()
    else:
        return dst_elem.pick_surface() + ' -> ' + make_root_path(sentence_l, dst_elem.dst)
##############################################################
   

#CaboChaの解析結果（neko.txt.cabocha）を読み込む
with open('neko.txt.cabocha')as f:
    f_list = f.readlines()#一行ずつ
    f_list = f_list[:-1]#EOS除去

    
morph_elem = [] 
chunk_elem = []
chunk_list = []
sentence_list = []

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

            
            

ans = '' #'述語\t格のリスト'の文字列
ans_list = []

#10文分
for s_l in sentence_list[:10]:
    srcs_str=''#係り元文節の文字列
    dst_str =''#係り先文節の文字列

    for chunk_e in s_l:
        #print(chunk_e.pick_surface())
        srcs_num = chunk_e.srcs
        dst_num  = chunk_e.dst
        path = ''
    
        if chunk_e.check_noun():                #まず係り元に名詞があること
            srcs_str = chunk_e.pick_surface()   #係り元の表層形
    
            ans = srcs_str + ' -> '             #係り元の表層形 ->
            path = make_root_path(sentence_list, dst_num)
            ans += path
            #print(ans)
            ans_list.append(ans)

'''
for i in ans_list[:20]:
    print(i)
    
一吾輩は -> 猫である
猫である -> 無い
名前は -> 無い
どこで -> 生れたか -> つかぬ
見当が -> つかぬ
何でも -> 薄暗い -> 所で -> 泣いて -> 記憶している
所で -> 泣いて -> 記憶している
ニャーニャー -> 泣いて -> 記憶している
いた事だけは -> 記憶している
記憶している -> 見た
吾輩は -> 見た
ここで -> 始めて -> 人間という -> ものを -> 見た
人間という -> ものを -> 見た
ものを -> 見た
あとで -> 聞くと -> 種族であったそうだ
それは -> 種族であったそうだ
書生という -> 人間中で -> 種族であったそうだ
人間中で -> 種族であったそうだ
一番 -> 獰悪な -> 種族であったそうだ
獰悪な -> 種族であったそうだ

'''