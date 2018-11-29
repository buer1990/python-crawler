# -*- coding: utf-8 -*-#
import urllib.request
import chardet
#-------------------------------------------------------------------------------
# Name:         chardetTest
# Description:  
# Author:       buer1990
# Date:         2018/11/22
#-------------------------------------------------------------------------------

# print("Helloworld!")
# print("你好世界!")
if '__name__' == '__main__':
    str="http://www.baidu.com"
    re=request.urlopen(str).read().decode('utf-8')

    charset=chardet.detect(re)
    print(charset)