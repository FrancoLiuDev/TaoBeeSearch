import os
import json
import requests
from bs4 import BeautifulSoup
import pandas
import re

URL = 'https://s.taobao.com/search?q=%E8%BF%9E%E8%BA%AB%E8%A3%99&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170711&ie=utf8'

pageConfig = None

def mainPaser(url):

    global pageConfig
    Headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36"}
    Response = requests.get(url, headers=Headers)
    Interial = BeautifulSoup(Response.content, 'html.parser')
    pageConfig = Interial.find('script', text=re.compile('g_page_config'))
    return pageConfig.string

info = mainPaser(URL)
 
neededColumns = ['category', 'comment_count', 'item_loc', 'nick', 'raw_title', 'view_price', 'view_sales']
gPageConfig = re.search(r'g_page_config = (.*?);\n', pageConfig.string)
pageConfigJson = json.loads(gPageConfig.group(1))
pageItems = pageConfigJson['mods']['itemlist']['data']['auctions']
pageItemsJson = json.dumps(pageItems)
 
pageData = pandas.read_json(pageItemsJson)
neededData = pageData[neededColumns]
 