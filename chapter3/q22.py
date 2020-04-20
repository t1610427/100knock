# coding:utf-8
import re

fname = "uk_text.txt"
category_name_list = []

with open(fname,'r',encoding="utf-8_sig") as f:
    for f_line in f:
        category_name = re.search(r"^\[\[Category:(\w+・*\w+)|(\w+\|)\]\]",f_line)
        if category_name != None:   #文字列内にパターンにマッチする場所がなければNone
            category_name_list.append(category_name.group(1))

print(category_name_list)

'''
実行結果
['イギリス', '英連邦王国', 'G8加盟国', '欧州連合加盟国', '海洋国家', '君主国', '島国', '1801年に設立された州・地域']
'''


'''
行単位ではなく名前で抽出
[[Category:イギリス|*]]のイギリスだけを表示すればよい
-->[[Category:XX|*]]パターン1
-->[[Category:XXXX]]パターン2
-->[[Category:XX|x]]パターン3
-->[[Category:X・X]]パターン4
の4通りがある

Pythonは正規表現ベースの2つの異なる基本的な関数、
文字列の先頭でのみのマッチを確認する re.match() および、
文字列中の位置にかかわらずマッチを確認するre.search()を提供している。

re.search(pattern, string, flags=0)
stringを走査し,正規表現patternがマッチを生じさせる最初の場所を探して
対応する""マッチオブジェクト""を返します。
文字列内にパターンにマッチする場所がなければ None を返します。

マッチオブジェクト
(...)
丸括弧でグループの開始と終了 #'('をマッチするには、\(か文字クラス中に囲む[()]

\w
Unicode.単語文字にマッチ。これはあらゆる言語で単語の一部になりうるほとんどの文字、数字、およびアンダースコアを含む

+
直前の正規表現を 1 回以上繰り返したものにマッチさせる結果の正規表現にします。
例えばab+は'a'に1つ以上の'b'が続いたものにマッチ、単なる'a'にはマッチしません。

*
直前の正規表現を0回以上,できるだけ多く繰り返したものにマッチさせる結果の正規表現にします
ab* は 'a'、'ab'、または 'a' に任意個数の 'b' を続けたものにマッチします。

^
(キャレット)文字列の先頭にマッチ

|
A と B を任意の正規表現として、 A|B は A と B のいずれかにマッチする正規表現を作成します


>>> m = re.match(r"(\w+) (\w+)", "Isaac Newton, physicist")
>>> m.group(0)       # The entire match
'Isaac Newton'
>>> m.group(1)       # The first parenthesized subgroup.
'Isaac'
>>> m.group(2)       # The second parenthesized subgroup.
'Newton'
>>> m.group(1, 2)    # Multiple arguments give us a tuple.
('Isaac', 'Newton')
'''