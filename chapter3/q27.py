# coding:utf-8
import re
import pprint

fname = "uk_text.txt"
base_info_dic = {}

with open(fname,'r',encoding="utf-8_sig") as f:
    for f_line in f:        
        base_info = re.search(r"^\|(?P<field_name>.*?)\s=\s(?P<field_val>.*)",f_line) 
        if base_info != None:
            removed_markup = re.sub(r"\'{2,5}(\w+)\'{2,5}", lambda m: m.group(1),               base_info.group('field_val'))   #'2～5個に挟まれた文字を文字のみに置換 
            removed_link   = re.sub(r"\[{2}(.+?)\]{2}",     lambda m: m.group(1).split("|")[-1],removed_markup)                 #マッチしたグルー1の|区切の後ろ側を取得
            #P47.縦の線、P42似ているコードは似ているように
            base_info_dic[base_info.group('field_name')] = removed_link
            
pprint.pprint(base_info_dic)


'''
実行結果
{'GDP/人': '36,727<ref name="imf-statistics-gdp" />',
 'GDP値': '2兆3162億<ref name="imf-statistics-gdp" />',
 'GDP値MER': '2兆4337億<ref name="imf-statistics-gdp" />',
 'GDP値元': '1兆5478億<ref '
          'name="imf-statistics-gdp">[http://www.imf.org/external/pubs/ft/weo/2012/02/weodata/weorept.aspx?pr.x=70&pr.y=13&sy=2010&ey=2012&scsm=1&ssd=1&sort=country&ds=.&br=1&c=112&s=NGDP%2CNGDPD%2CPPPGDP%2CPPPPC&grp=0&a= '
          'IMF>Data and Statistics>World Economic Outlook Databases>By '
          'Countrise>United Kingdom]</ref>',
 'GDP統計年': '2012',
 'GDP統計年MER': '2012',
 'GDP統計年元': '2012',
 'GDP順位': '6',
 'GDP順位MER': '5',
 'ISO 3166-1': 'GB / GBR',
 'ccTLD': '.uk / .gb<ref>使用は.ukに比べ圧倒的少数。</ref>',
 '人口値': '63,181,775<ref>[http://esa.un.org/unpd/wpp/Excel-Data/population.htm '
        'United Nations Department of Economic and Social Affairs>Population '
        'Division>Data>Population>Total Population]</ref>',
 '人口大きさ': '1 E7',
 '人口密度値': '246',
 '人口統計年': '2011',
 '人口順位': '22',
 '位置画像': 'Location_UK_EU_Europe_001.svg',
 '元首等氏名': 'エリザベス2世',
 '元首等肩書': '女王',
 '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern '
         'Ireland}}<ref>英語以外での正式国名:<br/>',
 '公用語': '英語（事実上）',
 '国旗画像': 'Flag of the United Kingdom.svg',
 '国歌': '神よ女王陛下を守り給え',
 '国章リンク': '（国章）',
 '国章画像': 'イギリスの国章',
 '国際電話番号': '44',
 '夏時間': '+1',
 '建国形態': '建国',
 '日本語国名': 'グレートブリテン及び北アイルランド連合王国',
 '時間帯': '±0',
 '最大都市': 'ロンドン',
 '標語': '{{lang|fr|Dieu et mon droit}}<br/>（フランス語:神と私の権利）',
 '水面積率': '1.3%',
 '注記': '<references />',
 '略名': 'イギリス',
 '確立年月日1': '927年／843年',
 '確立年月日2': '1707年',
 '確立年月日3': '1801年',
 '確立年月日4': '1927年',
 '確立形態1': 'イングランド王国／スコットランド王国<br />（両国とも1707年連合法まで）',
 '確立形態2': 'グレートブリテン王国建国<br />（1707年連合法）',
 '確立形態3': 'グレートブリテン及びアイルランド連合王国建国<br />（1800年連合法）',
 '確立形態4': '現在の国号「グレートブリテン及び北アイルランド連合王国」に変更',
 '通貨': 'UKポンド (&pound;)',
 '通貨コード': 'GBP',
 '面積値': '244,820',
 '面積大きさ': '1 E11',
 '面積順位': '76',
 '首相等氏名': 'デーヴィッド・キャメロン',
 '首相等肩書': '首相',
 '首都': 'ロンドン'}
'''
            
'''
[[記事名]]-->[[(|)記事名]]-->記事名
[[記事名|表示文字]]-->表示文字
[[記事名#節名|表示文字]]-->表示文字
大きく3パターン

'確立年月日1': '[[927年]]／[[843年]]',
'ccTLD': '[[.uk]] / [[.gb]]
'首相等氏名': '[[デーヴィッド・キャメロン]]',
'国章画像': '[[ファイル:Royal Coat of Arms of the United Kingdom.svg|85px|イギリスの国章]]',
の考慮

re.sub(pattern, repl, string, count=0, flags=0)
string中に出現する最も左の重複しないpatternを置換replで置換することで得られる文字列を返す。
パターンが見つからない場合stringがそのまま返される。

[^5]は5をのぞくすべての文字。^は集合の最初の文字でなければ特別の意味を持ちません。

'''