# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         changeUserAgentTest
# Description:  
# Author:       buer1990
# Date:         2018/11/23
#-------------------------------------------------------------------------------
from urllib import request

if __name__ == '__main__':
    url='http://www.csdn.net'
    head={}
    head['User Agent']='Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19'
    req=request.Request(url=url,headers=head)
    response=request.urlopen(req)
    print(response.info())
    html=response.read().decode('utf-8')
    print(html)