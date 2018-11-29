# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         CookieMomi
# Description:  
# Author:       buer1990
# Date:         2018/11/27
#-------------------------------------------------------------------------------
from http import cookiejar
from urllib import request

if __name__ == '__main__':
     #创建一个cookiejar 对象实例
     cookie=cookiejar.CookieJar()
     #利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
     cookiehandler=request.HTTPCookieProcessor(cookie)
     opener=request.build_opener(cookiehandler)
     #使用自建opener方法打开网页
     res=opener.open("http://www.baidu.com")
     #打印cookie信息
     for item in cookie:
         print('Name= %s'% item.name)
         print('value= %s'% item.value)