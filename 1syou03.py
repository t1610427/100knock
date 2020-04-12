target = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
ans = []
tem = []     #空白区切で分解した単語リスト
tango = []   #','と'.'を除いた単語リスト
i=0

tem = target.split()         #空白区切りで文を分割
while i < len(tem):
    tango.append( tem[i].strip(',''.') )        #','と'.'を除く
    i += 1

i=0
while i < len(tango):
    ans.append( len(tango[i]) )                 #文字数をansに格納
    i += 1

print("answer:{}".format(ans))