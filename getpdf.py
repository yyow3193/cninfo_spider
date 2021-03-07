
import requests
import random
import time
import urllib
import json
import re

download_path = 'http://www.cninfo.com.cn/'
pdf_saving_path = './pdf/'

User_Agent = [
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 2.0.50727; Media Center PC 6.0)",
    "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; .NET CLR 1.0.3705; .NET CLR 1.1.4322)",
    "Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
    "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN; rv:1.9) Gecko/20080705 Firefox/3.0 Kapiko/3.0"
]


headers = {
            "User-Agent": "Fiddler Everywhere",
            "Host": "www.gintong.com",
            "Content-Type": "application/json"
           }




def getpdf():
    query_path = 'http://www.gintong.com/searchServer/bigData/search/getAnnouncement'
    headers['User-Agent'] = random.choice(User_Agent)  # 定义User_Agent
    query = {
             "keyword":"603977.SH",
             "pno":"1",
             "psize":"20",
             "startTime":"2020-07-01",
             "endTime":"2020-08-20",
             "title":"报"
            }

    itemlist = requests.post(query_path, headers=headers, data=json.dumps(query))
    print(itemlist.text)
    #dict_str = json.loads(itemlist.text)
    #print(dict_str)
    
getpdf()


