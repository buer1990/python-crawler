# -*- coding: utf-8 -*-#

# -------------------------------------------------------------------------------
# Name:         t8
# Description:  
# Author:       buer1990
# Date:         2019/1/18
# -------------------------------------------------------------------------------
import random

from lxml import etree
import requests
url='https://movie.douban.com/'
Ua_list=['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41',
         ]
ua=random.choice(Ua_list)
headers={'User-agent': ua}
res=requests.get(url=url,headers=headers)
with res:
    content=res.text
    # print(html)
    html=etree.HTML(content)
    titles=html.xpath("//div[@class='billboard-bd']//tr/td/a/text()")
    urls=html.xpath("//div[@class='billboard-bd']//tr/td/a")#豆瓣一周热评电影连接
    #
    # i=0
    # for title in titles:
    #     i = i + 1
    #     print(i,'.',title,':',urls[i-1].get('href'))

"""
获取top10 热短评主页连接和热长评主页连接
"""
urlhps=[]
urllps=[]
for urlP in urls:
    with requests.get(url=urlP.get('href'),headers=headers) as res:
        contentP=res.text
        htmlP=etree.HTML(contentP)
        url1 = res.url

        # 获取电影评短热评
        elementP=htmlP.xpath("//*[@id ='hot-comments']/a")
        url2=elementP[0].get('href')
        urlhp='{}{}'.format(url1,url2)
        urlhps.append(urlhp)

        # 获取电影长热评连接
        elementlp = htmlP.xpath("//section[@ class='reviews mod movie-content']/p/a")
        urll2 = elementlp[0].get('href')
        urllp = '{}{}'.format(url1, urll2)
        urllps.append(urllp)

"""
获取热热长评内容页
"""
urllpcc={}
for urllp in urllps:
    with requests.get(url=urllp, headers=headers) as res:
        contentP = res.text
        htmlP = etree.HTML(contentP)
        review_list_element = htmlP.xpath("//div[@class='main-bd']/h2/a")
        tilename = htmlP.xpath("//div[@class='main-bd']/h2/a/text()")
        # print(tilename)
        i=0
        for name in tilename:
            urllpcc[name]=review_list_element[i].get('href')
            # print(review_list_element[i].get('href'))
            i = i + 1

for name,urll in urllpcc.items():
    with requests.get(urll) as res:
        con=res.text
        html=etree.HTML(con)
        conts=html.xpath("//div[@class='review-content clearfix']/p/text()")
        print('准备写入==>',name)
        name1=str(name).replace(' ', '')
        name2=str(name1).replace('?','')
        name3=str(name2).replace('\n','')
        with open('d:/douban/{}.txt'.format(str(name2).replace(' ','')), mode='w+', encoding='utf-8') as  f:
            f.write(name+'\n\n')
            for txt in conts:
                f.write(txt+'\n')
            print('·'*21)
            f.flush()
        print('写入完成!')
print('爬取全部完成！')