target="Hi He Lied Because Boron Could Not Oxidize Fluorine. \
New Nations Might Also Sign Peace Security Clause. \
Arthur King Can."

word=[]         #文を単語に分解した時の単語リスト
top=[]          #単語から先頭1文字あるいは2文字を取り出したリスト
ans={}          #1文字あるいは2文字とその文字の文における単語の位置
top_1=[1,5,6,7,8,9,15,16,19]
i=0
j=0

tmp = target.split()       #空白区切りで文を分割
while i < len(tmp):
    word.append( tmp[i].strip(',''.') )        #','と'.'を除く
    i += 1

i=0
while i < len(word):
    if i == top_1[j]-1:             #1,5,6,7,8,9,15,16,19番目の単語は先頭の1文字取り出し
        ans[word[i][0]] = i+1       #辞書型に先頭文字と何番目の単語かを格納
        if j < len(top_1)-1:
            j += 1
    else:
        ans[word[i][0:2]] = i+1     #辞書型に先頭2文字と何番目の単語かを格納
    i += 1

print(ans)