def cipher(str):
    ans=''
    for i in range(len(str)):
        if str[i].isupper():                    #大文字の判定
            ans+=str[i]
        else:
            tmp = ord(str[i])                   #アスキーコード取得
            tmp = chr(219-tmp)                  #アスキーコードから文字列へ
            ans+=tmp
    return ans
