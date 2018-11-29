# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         loadcookiefile
# Description:  
# Author:       buer1990
# Date:         2018/11/27
#-------------------------------------------------------------------------------
from http import cookiejar
from urllib import request

if __name__ == '__main__':
    filename='../resource/cookie1.txt'
    cookie=cookiejar.MozillaCookieJar()
    cookie.load(filename,ignore_expires=True,ignore_discard=True)
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookiehandler=request.HTTPCookieProcessor(cookie)
    opener=request.build_opener(cookiehandler)
    res=opener.open("http://fanyi.youdao.com/")
    print(res.read().decode('utf-8'))