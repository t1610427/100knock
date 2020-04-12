target1="パトカー"
target2="タクシー"
ans=''
i=0

#target1とtarget2の先頭から一文字ずつ取り出す
while i < len(target1):
    ans += target1[i]
    ans += target2[i]
    i += 1

print("answer:{}".format(ans))