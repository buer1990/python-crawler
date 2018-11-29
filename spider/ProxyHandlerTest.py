# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         ProxyHandlerTest
# Description:  
# Author:       buer1990
# Date:         2018/11/23
#-------------------------------------------------------------------------------
from urllib import request, error

if __name__ == '__main__':
    url='https://www.whatismyip.com/'
    proxy={'http':'119.97.70.143:8123'}
    #202.107.207.154
    #该网站同一ip请求多次会被拒掉
    #创建ProxyHandler
    Proxy_Handler=request.ProxyHandler(proxy)
    #创建opener
    opener=request.build_opener(Proxy_Handler)
    # 添加User Angent
    opener.addheaders=[('User-Agent','Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36')]
    #安装opener
    request.install_opener(opener)
    try:
        res=request.urlopen(url)
        html=res.read().decode('utf-8')
        print(html)
    except error.HTTPError as h:
        print(h.code)
    except error.ContentTooShortError as c:
        print(c.reason)