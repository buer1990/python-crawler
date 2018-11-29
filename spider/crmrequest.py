# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         crmrequest
# Description:  
# Author:       buer1990
# Date:         2018/11/28
#-------------------------------------------------------------------------------

from http import cookiejar
from urllib import request
from bs4 import BeautifulSoup
import re
if __name__ == '__main__':
        filename='../resource/crmadmincookies'
        # load cookies 请求其他页面
        cookies2 = cookiejar.MozillaCookieJar()
        cookies2.load(filename=filename, ignore_discard=True, ignore_expires=True)
        # 创建一个CookieHandler
        cookieHandler2 = request.HTTPCookieProcessor(cookies2)
        # 创建一个opener
        opener2 = request.build_opener(cookieHandler2)
        res2 = opener2.open('http://test.crmadmin.hipac.cn/admin/dataStatistic/shopInfo/show.do?_m_id=2331')
        html2 = res2.read().decode('utf-8')
        #print(html2)
        soup=BeautifulSoup(html2, "lxml")
        #print(soup)
        # print(soup.title.name)
        # print(soup.li)
        # for child in soup.body.children:
        #     print(child)
        print(soup.find_all('span'))

        for tag in soup.find_all(re.compile("^b")):
            print(tag.name)
