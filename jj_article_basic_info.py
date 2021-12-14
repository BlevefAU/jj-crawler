# import dependencies
# if using python2 may required set code utf-8
import requests
import json
import pymysql
import random
import datetime
import time
from bs4 import BeautifulSoup


def load_user_agents(file, pattern):
    list = []
    selection = []
    # load JSON file
    list = json.load(open(file))
    for item in list:
        if item['pattern'] == pattern:
            selection = item['instances']
            # remove the first define
            selection.pop(0)
    return selection


agents_list = load_user_agents('user_agents.json', 'Googlebot\\/')



url = 'https://www.jjwxc.net/onebook.php?novelid=1724503'


head = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    'AlexaToolbar-ALX_NS_PH': 'AlexaToolbar/alx-4.0',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6,ja;q=0.4',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'text/html',
}


#使用post会报错 (2021/5/2)
jscontent = requests \
    .session() \
    .get(url,headers=head) 

jscontent.encoding = 'gb18030'
html = jscontent.content
raw_data = BeautifulSoup(html, 'html.parser')

print(raw_data.find(id='novelintro').get_text())

# with open('test.txt', 'w', encoding="utf-8") as f:
#     f.write(html)
