# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         urllib_errorTest
# Description:  
# Author:       buer1990
# Date:         2018/11/23
#-------------------------------------------------------------------------------
from urllib import request, error

if __name__ == '__main__':
    #访问一个不存在的连接
    # url="http://www.iloveyou.com"
    url='http://www.youdao.com/fang.html'
    try:
        res=request.urlopen(url)
        html=res.read().decode('utf-8')
        print(html)
    # except error.URLError  as e:
    #     print(e.reason)
    except error.HTTPError as h:
        print(h.code,h.reason)

