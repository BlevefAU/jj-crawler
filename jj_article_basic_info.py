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

# modify the required number here (start, end)
for novelid in range(1724503, 1724505):
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
        try:
            # modify here to write the data into file
            # -----------------------------
            # title
            print(raw_data.find("span",class_="bigtext").get_text())
            # description
            print(raw_data.find(id='novelintro').get_text())
            # article type
            print(raw_data.find("span", itemprop="genre").get_text())
            print("________________________")
            # -----------------------------

        except Exception as e:
            # if encounter error means the article is deleted or other error
            print(e)

        # if you want to import into sql database, uncomment this part and modify it
        # -----------------------------
        # try:
        #     conn = pymysql.connect(
        #     host='localhost', user='root', passwd='root', db='jjwxc', charset='utf8')   
        # except Exception as e:
        #     print(e)
        # -----------------------------

    except Exception as e:
        # eles print error and pass
        print(e)
        pass
