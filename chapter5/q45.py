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
    
    ###################################
    #文節の中から動詞の原形を返す
    def pick_verb(self):
        for i in self.morphs:
            if i.pos == '動詞':
                return i.base
        return None
    
    #文節の中から助詞の原形を返す
    def pick_particle(self):
        for i in self.morphs:
            if i.pos == '助詞':
                return i.base
        return None
    ###################################
    
    
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

    ###################################   
    # その文節に助詞が含まれるならTrue、ないならFalse 
    def check_particle(self):
        for i in self.morphs:
            if i.pos == '助詞':
                return True
        return False
    ###################################
    
    
def make_morph(file_line):
    surface  = file_line.split('\t')[0]
    result_r = file_line.split('\t')[1]
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

###########################################################
#与えられた文節番号に一致する係り先文節番号を持つ文節（複数）のリストを返す
def pick_srcsElem_from_srcsNum(sentence_l, srcs_num):
    srcs_elements = []
    for chunk_e in sentence_l:
        if chunk_e.dst == srcs_num:
            srcs_elements.append(chunk_e)
    return srcs_elements

###########################################################
    
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
            morph_elem.append(result)
        else:
            morph_elem.append(result)
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
        srcs_num = chunk_e.srcs
        dst_num  = chunk_e.dst

        
        if chunk_e.check_verb():#係り先が動詞を含む文節の時だけを見る
            dst_str = chunk_e.pick_verb()#係り先の動詞の原形
            srcs_elems = pick_srcsElem_from_srcsNum(s_l, srcs_num) #係り元文節のリスト
            
            if srcs_elems != []:
                particle_l=[]               #助詞文字列のリスト
                
                for srcs_elem in srcs_elems:
                    if srcs_elem.check_particle():                      #係り元文節に助詞があるときTrue
                        particle_l.append(srcs_elem.pick_particle())    #助詞文字列のリストに格納していく

                srcs_str = ' '.join(i for i in particle_l)#係り元の助詞たちを空白区切で文字列にする
                
                if srcs_str != '':
                    ans = dst_str + '\t' + srcs_str 
                    ans_list.append(ans)

'''
for i in ans_list[:20]:
    print(i)
生れる  で
つく    か が
泣く    で
する    て だけ
始める  で
見る    は を
聞く    で
捕える  を
煮る    て
食う    て
思う    から
載せる  に
持ち上げる      て と
ある    が
落ちつく        で
見る    て を
見る    の
'''