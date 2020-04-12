str1="paraparaparadise"
str2="paragraph"

#n-gramを作る関数
def ngram(str, n):
    ans = []
    for i in range( len(str)-n+1):
        ans.append(str[i:i+n])
    return ans

X = ngram(str1, 2)
Y = ngram(str2, 2)

X_set = set(X)
Y_set = set(Y)

XY_union        = X_set | Y_set                 #和集合
XY_intersection = X_set.intersection(Y_set)     #積集合
XY_difference   = X_set.difference(Y_set)       #差集合

se = {"se"}
print(se <= X_set)
print(se.issubset(Y_set))