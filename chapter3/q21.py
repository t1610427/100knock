# coding:utf-8
import pprint

fname = "uk_text.txt"
category_dic={}         #カテゴリ名を宣言している行を抽出-->{"行数":"カテゴリ名"}

with open(fname,'r',encoding="utf-8_sig") as f:
    for i, f_line in enumerate(f):   
        if 'Category' in f_line:        #inは部分一致
            category_dic[i+1]=f_line.strip("\n")
            
pprint.pprint(category_dic)   

'''
実行結果
{522: '[[Category:イギリス|*]]',
 523: '[[Category:英連邦王国|*]]',
 524: '[[Category:G8加盟国]]',
 525: '[[Category:欧州連合加盟国]]',
 526: '[[Category:海洋国家]]',
 527: '[[Category:君主国]]',
 528: '[[Category:島国|くれいとふりてん]]',
 529: '[[Category:1801年に設立された州・地域]]'}
'''


'''
部分一致、すなわち、ある文字列の中にもう一方の文字列が含まれているかどうかの判定にはin演算子を使う。
x in yとしたとき、xがyに含まれているとTrue
print('bbb' in 'aaa-bbb-ccc')
#-->True
print('xxx' in 'aaa-bbb-ccc')
#-->False

print('xxx' not in 'aaa-bbb-ccc')
#-->True

522行目から529行目に
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
'''