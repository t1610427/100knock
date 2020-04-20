# coding:utf-8
import json
import gzip

fname = 'jawiki-country.json.gz'
uk_text=''
with gzip.open(fname, 'rt',encoding="utf-8_sig") as json_f: #rtでテキスト用。エンコーディング指定
    for json_line in json_f:                                #一行に一つの国の辞書型。記事名が"title"キー，記事本文が"text"キー
        json_data = json.loads(json_line)
        
        if json_data['title'] == 'イギリス':
            print(json_data['text'])            #イギリスに関する記事本文の表示
            uk_text = json_data['text']         #21-29で使うためuk_textに格納
            break

with open('uk_text.txt','w') as f:              #イギリスのみのファイル作成
    f.write(uk_text) 

     

'''
実行結果
{{redirect|UK}}
{{基礎情報 国
|略名 = イギリス
|日本語国名 = グレートブリテン及び北アイルランド連合王国
|公式国名 = {{lang|en|United Kingdom of Great Britain and Northern Ireland}}<ref>英語以外での正式国名:<br/>
*{{lang|gd|An Rìoghachd Aonaichte na Breatainn Mhòr agus Eirinn mu Thuath}}（[[スコットランド・ゲール語]]）<br/>
*{{lang|cy|Teyrnas Gyfunol Prydain Fawr a Gogledd Iwerddon}}（[[ウェールズ語]]）<br/>
.
.
.
{{デフォルトソート:いきりす}}
[[Category:イギリス|*]]
[[Category:英連邦王国|*]]
[[Category:G8加盟国]]
[[Category:欧州連合加盟国]]
[[Category:海洋国家]]
[[Category:君主国]]
[[Category:島国|くれいとふりてん]]
[[Category:1801年に設立された州・地域]]
'''



'''
jawiki-wountry.jsonの構成
{"text":"...\n...\n...", "title":"ドイツ"}
{"text":"...\n...\n...", "title":"イギリス"}
{"text":"...\n...\n...", "title":"ラトビア"}
辞書型でtextとtitleの二つのキーを持っている
1行で書かれている
1:エジプト
2:オーストリア
3:インドネシア
.
.
196:ドイツ
197:イギリス

gzip.open
gzip 圧縮ファイルをバイナリまたはテキストモードで開き、ファイルオブジェクト を返す。
'''