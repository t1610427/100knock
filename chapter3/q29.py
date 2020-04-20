# coding:utf-8
import re
import pprint
import requests

fname = "uk_text.txt"
base_info_dic = {}

with open(fname,'r',encoding="utf-8_sig") as f:
    for f_line in f:        
        base_info = re.search(r"^\|(?P<field_name>.*?)\s=\s(?P<field_val>.*)",f_line) 
        if base_info != None:
            base_info_dic[base_info.group('field_name')] = base_info.group('field_val')

#ここまではq25.py
            
########################################################################
#https://www.mediawiki.org/wiki/API:Imageinfo/ja#GET_リクエスト.を参考

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "prop": "imageinfo",
    "iiprop": "url",     #Gives URL to the file and the description page.ファイルと説明ページへのURLを提供。
    "titles": "File:" + base_info_dic['国旗画像']
}

R = requests.get(url=URL, params=PARAMS)
DATA = R.json()
PAGES = DATA["query"]["pages"]
pprint.pprint(PAGES)

for k, v in PAGES.items():
    print(v["title"], v["imageinfo"][0]["url"])

'''
実行結果
{'23473560': {'imageinfo': [{'descriptionshorturl': 'https://en.wikipedia.org/w/index.php?curid=23473560',
                             'descriptionurl': 'https://en.wikipedia.org/wiki/File:Flag_of_the_United_Kingdom.svg',
                             'url': 'https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg'}],
              'imagerepository': 'local',
              'ns': 6,
              'pageid': 23473560,
              'title': 'File:Flag of the United Kingdom.svg'}}
File:Flag of the United Kingdom.svg https://upload.wikimedia.org/wikipedia/en/a/ae/Flag_of_the_United_Kingdom.svg

'''