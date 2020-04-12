target = "stressed"
ans = ''
i = len(target) - 1

#targetの末尾から一文字ずつ連結していく
while 0 <= i:
    ans += target[i]
    i -= 1