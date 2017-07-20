import os
import json
import requests
from bs4 import BeautifulSoup
import pandas
import re

url = 'https://s.taobao.com/search?q=%E8%BF%9E%E8%BA%AB%E8%A3%99&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170711&ie=utf8'
res = requests.get('https://s.taobao.com/search?q=%E8%BF%9E%E8%BA%AB%E8%A3%99&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170711&ie=utf8')

soup = BeautifulSoup(res.text, 'html.parser')


content = res.content.decode('utf-8')
 
items = pandas.Series()

mydivs = soup.findAll("div")
  
regex = 'g_page_config = (.+)'
        
items = re.findall(regex, content)
print items
items = items.pop().strip()
items = items[0:-1]
items = json.loads(items)
 

items = items['mods']['itemlist']['data']['auctions']
for item in items:

    if 'item_loc' in item:
        item_loc = item['item_loc'].encode('utf-8')
    else:
        item_loc = u" "
    if 'nick' in item:
        nick = item['nick'].encode('utf-8')
    else:
        nick = u" "
    if 'raw_title' in item:
        raw_title = item['raw_title'].encode('utf-8')
    else:
        raw_title = u" "
    if 'view_sales' in item:
        view_sales = item['view_sales'].encode('utf-8')
    else:
        view_sales = u" "
    if 'view_price' in item:
        view_price = item['view_price'].encode('utf-8')
    else:
        view_price = u" "
    if 'comment_url' in item:
        comment_url = item['comment_url'].encode('utf-8')
    else:
        comment_url = u" "
    comment_url = 'https:'+comment_url
    
    #chi = item_loc.encode('gb2312')
     
    
    print("{0}——{1}——{2}——{3}——{4}".format(item_loc, nick, raw_title, view_sales, view_price))
    #fd.write((item_loc+','+nick+','+raw_title+','+view_sales+','+view_price+','+comment_url + u"\n"))