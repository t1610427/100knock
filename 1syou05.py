target = "I am an NLPer"

def ngram(str,n):
    ans = []
    for i in range( len(str)-n+1):
        ans.append(str[i:i+n])
    return ans

#単語bi-gram
word = target.split()           #空白区切りで単語を分割
word_bigram = ngram(word,2)
print(word_bigram)

#文字bi-gram
str_bigram = ngram(target,2)
print(str_bigram)

