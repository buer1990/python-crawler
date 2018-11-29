# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         crawltxtBook
# Description:  
# Author:       buer1990
# Date:         2018/11/28
#-------------------------------------------------------------------------------
from urllib import request
from bs4 import BeautifulSoup
if __name__ == '__main__':
     url='http://www.biqukan.com/1_1094/5403177.html'
     head={'User-Agent':'Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166  Safari/535.19'}
     req=request.Request(url=url,headers=head)
     res=request.urlopen(req)
     html=res.read().decode('gbk','ignore')
     soup_texts =BeautifulSoup(html,'lxml')
     # print(soup_texts.body)
     texts = soup_texts.find_all(id='content', class_='showtxt')
     print(texts)
     soup_text = BeautifulSoup(str(texts), 'lxml')
     # 将\xa0无法解码的字符删除
     print(soup_text.div.text.replace('\xa0', ''))