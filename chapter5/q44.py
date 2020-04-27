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

############################################
file_count = 1
#与えられた'係り元文節\t係り先文節'をDOT言語に変換する
def write_dot_file(ans_l):
    global file_count
    text = "digraph graph_name {"
    for i in ans_l:
        text += "{}->{};".format(*i.split())
    text += "}"
    #print(text)
    
    with open("q44_{}.dot".format(file_count),'w')as f:
        f.write(text)
    file_count += 1
################################################### 



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

            
            
srcs_str=''#係り元文節の文字列
dst_str =''#係り先文節の文字列
ans = '' #'係り元\t係り先'の文字列
ans_list = []

#50文分
for s_l in sentence_list[:50]:
    for chunk_e in s_l:
        dst_num  = chunk_e.dst
        srcs_str = chunk_e.pick_surface()

        dst_elem = pick_dstElem_from_dstNum(sentence_list, dst_num)

        dst_str  = dst_elem.pick_surface()
        ans = srcs_str + '\t' + dst_str
        ans_list.append(ans)

#ここまでは42.pyと同じ
#################################

write_dot_file(ans_list[0:10])
write_dot_file(ans_list[10:35])

################################
#Ubuntuの方でコマンド実行
#$dot -Tpng q44_1.dot -o q44_1.png
#$dot -Tpng q44_2.dot -o q44_2.png
