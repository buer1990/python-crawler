# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         saveCookie2file
# Description:  
# Author:       buer1990
# Date:         2018/11/27
#-------------------------------------------------------------------------------
from http import cookiejar
from urllib import request, error

if __name__ == '__main__':
     #设置cookie存放的文件
     filename='../resource/cookie1.txt'
     #生成一个MozillaCookieJar对象实例来保存cookie，之后写入文件
     cookie=cookiejar.MozillaCookieJar(filename)
     # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
     cookiehamdler=request.HTTPCookieProcessor(cookie)
     opener=request.build_opener(cookiehamdler)
     try:
        res=opener.open("http://fanyi.youdao.com/")
     except error.HTTPError as h:
         print(h.code)
     cookie.save(filename=filename,ignore_discard=True,ignore_expires=True)

