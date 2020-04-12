import random

#4文字以上の与えられた文字列の先頭と最後以外を並び替える関数
def middle_shuffle(str):
    tmp = []
    if 4<=len(str):
        tmp+=str[0]
        tmp+=random.sample(str[1:-1], len(str[1:-1]))   #先頭と最後の文字以外をランダムに並び替え
        tmp+=str[-1]
        return ''.join(tmp)
    else:
        return str

target = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
word = target.split()   #空白区切りで分解
ans=[]
for i in range(len(word)):
    ans.append( middle_shuffle(word[i]) )

' '.join(ans)