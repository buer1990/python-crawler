# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         fangyiTest
# Description:  
# Author:       buer1990
# Date:         2018/11/22
#-------------------------------------------------------------------------------
from urllib import request

if __name__ == '__main__':
    str="http://fanyi.baidu.com/"
    req=request.Request(str)
    response=request.urlopen(req)
    print(response.info())
    print(response.geturl())
    print(response.getcode())
    print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@\n\n")
    html=response.read().decode('utf-8')
    print(html)
