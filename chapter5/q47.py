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
    
    ####################################
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
    ###################################33
    
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
for s_l in sentence_list:
    srcs_str=''#係り元文節の文字列
    dst_str =''#係り先文節の文字列

    for chunk_e in s_l:
        srcs_num = chunk_e.srcs
        dst_num  = chunk_e.dst
    
        if chunk_e.check_verb():#まず係り先が動詞であること
            dst_str = chunk_e.pick_verb()
            
            srcs_elems = pick_srcsElem_from_srcsNum(s_l, srcs_num) #その文節にかかる文節のリスト

            if srcs_elems != []:
                particle_l=[]
                srcs_surface_l =[]#係り元の表層形のリスト
                
                for srcs_elem in srcs_elems:            #係り元の要素をひとつずつ見ていく               
                    if srcs_elem.check_particle_wo():   #次に係り元に助詞('を')があること
                        if srcs_elem.check_sa():        #さらに係り元がサ変であること

                            srcs_surface_l.append(srcs_elem.pick_surface())
                            particle_l.append(srcs_elem.pick_particle())
                
                srcs_str = ' '.join(i for i in particle_l) #係り元の助詞を文字列にする
                if srcs_str != '':
                    ans = dst_str + '\t' + srcs_str + '\t' + ' '.join(i for i in srcs_surface_l)
                    ans_list.append(ans)

'''
for i in ans_list[:20]:
    print(i)
する	を	決心を
する	を	返報を
する	を	昼寝を
する	を	昼寝を
加える	を	迫害を
する	を	家族的生活を
する	を	話を
する	を	投書を
する	を	話を
する	を	写生を
する	を	昼寝を
禁じる	を	失笑するのを
見る	を	彩色を
する	を	欠伸を
する	を	報道を
する	を	挨拶を
食う	を	御馳走を
する	を	問答を
する	を	雑談を
繰り返す	を	自慢話しを
'''