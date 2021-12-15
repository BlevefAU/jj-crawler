# import dependencies
# if using python2 may required set code utf-8
import requests
import json
import pymysql
import random
import datetime
import time
from bs4 import BeautifulSoup


# read agents function
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


# pick up pattern in agent list
agents_list = load_user_agents('user_agents.json', 'Googlebot\\/')

# modify the required number here
for novelid in range(1724500, 1724505):
    url = 'https://www.jjwxc.net/onebook.php?novelid='+str(novelid)
    head = {
        'User-Agent': random.choice(agents_list),
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'text/html',
    }
    result = requests \
        .session() \
        .get(url, headers=head)

    # jjwxc using gb18030 as html encoding (2021)
    result.encoding = 'gb18030'
    html = result.content

    # convert to html
    raw_data = BeautifulSoup(html, 'html.parser')

    try:
        # if the article data exist
        raw_data.find(id='oneboolt')
        
        print(raw_data.find("span",class_="bigtext").get_text())
        print(raw_data.find(id='novelintro').get_text())
        print(raw_data.find("span", itemprop="genre").get_text())

        print("________________________")

        # try:
        #     conn = pymysql.connect(
        #     host='localhost', user='root', passwd='root', db='jjwxc', charset='utf8')   
        # except Exception as e:
        #     print(e)
    except Exception as e:
        # eles print error and pass
        print(e)
        pass
