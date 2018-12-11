# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         requestsTest
# Description:  
# Author:       buer1990
# Date:         2018/11/29
#-------------------------------------------------------------------------------
import requests
from bs4 import BeautifulSoup
if __name__ == '__main__':
    target = 'http://www.biqukan.com/1_1094/5403177.html'
    req = requests.get(url=target)
    html=req.text
    bf = BeautifulSoup(html)
    texts = bf.find_all('div',class_='showtxt')
    print(texts)