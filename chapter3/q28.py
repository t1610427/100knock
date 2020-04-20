# coding:utf-8
import re
import pprint

fname = "uk_text.txt"
base_info_dic = {}

with open(fname,'r',encoding="utf-8_sig") as f:
    for f_line in f:        
        base_info = re.search(r"^\|(?P<field_name>.*?)\s=\s(?P<field_val>.*)",f_line) 
        if base_info != None:
            removed_markup = re.sub(r"\'{2,5}(\w+)\'{2,5}", lambda m: m.group(1),base_info.group('field_val'))  #'2～5個に挟まれた文字を文字のみに置換 
            removed_link = re.sub(r"\[{2}(.+?)\]{2}", lambda m: m.group(1).split("|")[-1],removed_markup)
            removed_angle_brackets = re.sub(r"<.*>", r"", removed_link) #<>で囲まれたものを除去
            base_info_dic[base_info.group('field_name')] = removed_angle_brackets
            
pprint.pprint(base_info_dic)

'''
実行結果
{'GDP/人': '36,727',
 'GDP値': '2兆3162億',
 'GDP値MER': '2兆4337億',
 'GDP値元': '1兆5478億',
 'GDP統計年': '2012',
 'GDP統計年MER': '2012',
 'GDP統計年元': '2012',
 'GDP順位': '6',
 'GDP順位MER': '5',
 'ISO 3166-1': 'GB / GBR',
 'ccTLD': '.uk / .gb',
 '人口値': '63,181,775',
 '人口大きさ': '1 E7',
 '人口密度値': '246',
 '人口統計年': '2011',
 '人口順位': '22',
 '位置画像': 'Location_UK_EU_Europe_001.svg',
 '元首等氏名': 'エリザベス2世',
 '元首等肩書': '女王',
 '公式国名': '{{lang|en|United Kingdom of Great Britain and Northern Ireland}}',
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
 '標語': '{{lang|fr|Dieu et mon droit}}（フランス語:神と私の権利）',
 '水面積率': '1.3%',
 '注記': '',
 '略名': 'イギリス',
 '確立年月日1': '927年／843年',
 '確立年月日2': '1707年',
 '確立年月日3': '1801年',
 '確立年月日4': '1927年',
 '確立形態1': 'イングランド王国／スコットランド王国（両国とも1707年連合法まで）',
 '確立形態2': 'グレートブリテン王国建国（1707年連合法）',
 '確立形態3': 'グレートブリテン及びアイルランド連合王国建国（1800年連合法）',
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