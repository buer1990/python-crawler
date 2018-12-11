# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         bs4Test
# Description:  
# Author:       buer1990
# Date:         2018/11/28
# -------------------------------------------------------------------------------
import re
from urllib import request
from bs4 import BeautifulSoup, element

if __name__ == '__main__':
    url = 'http://www.baidu.com/'
    req = request.Request(url)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # print(html)
    soup = BeautifulSoup(html, 'lxml')
    print(soup.title.string)
    print(soup.name)
    # print(soup.a.get['class'])
    print(soup.li)
    print(soup.li.string)
    print(type(soup.li.string))
    if type(soup.li.string) == element.NavigableString:
        print(soup.li.string)
    print('@@@@@@@@@@@@@@@@@@@@@@@@@@遍历html@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n')
    print(soup.body.contents[1])

    # for child in soup.body.children:
    #     print
    for a in soup.find_all('a'):
        print(a)
    for tag in soup.find_all(re.compile("^b")):
        print(tag.name)

    for tag in soup.find_all(True):
        print(tag.name)
    print(soup.find_all(attrs={'class': 'mnav'}))
    print(soup.find_all(text=re.compile("^百度")))
    print(soup.find_all(href_="javascript"))
