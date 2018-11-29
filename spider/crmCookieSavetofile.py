# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         crmCookieSavetofile
# Description:  
# Author:       buer1990
# Date:         2018/11/27
#-------------------------------------------------------------------------------
from http import cookiejar
from urllib import request, parse

if __name__ == '__main__':
     filename='../resource/crmadmincookies'
     url='http://************'
     #设置User-Agent，post参数，ip地址等
     user_agent=r'Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36'
     head={'User-Agnet': user_agent, 'Connection': 'keep-alive'}
     Login_Data={}
     Login_Data['deviceId']='********************'
     Login_Data['returnURL']='http%3A%2F%2Ftest.crmadmin.hipac.cn%2Fadmin%2FdataStatistic%2FshopInfo%2Fshow.do%3F_m_id%3D2331'
     Login_Data['userNickName']='***********'
     Login_Data['userPass']='****************'
     Login_Data['emailCode']='**************'
     Login_Data['publicKey']='**************'
     Login_Data['isApp']='false'
     Login_Data['os']='Windows 10 64-bit'
     Login_Data['app']='1'
     Login_Data['app_']='8dda532f2eafa8271d9f639eda5f71cc'
     Login_Data['osv']='10'
     Login_Data['model']='Chrome 68.0.3440.106 32-bit on Windows 10 64-bit'
     # 使用urlencode方法转换标准格式
     LoginPostData=parse.urlencode(Login_Data).encode('utf-8')
     # 生成一个MozillaCookieJar对象实例来保存cookie，之后写入文件
     cookies=cookiejar.MozillaCookieJar(filename)
     #创建一个CookieHandler
     cookieHandler=request.HTTPCookieProcessor(cookies)
     #创建一个opener
     opener=request.build_opener(cookieHandler)
     # 创建Request对象
     req=request.Request(url=url,data=LoginPostData,headers=head)
     #使用自建opener请求网页
     res=opener.open(req)
     cookies.save(ignore_discard=True,ignore_expires=True)
     html=res.read().decode('utf-8')
     print("~~~~~~~~~~~~~~~分割线~~~~~~~~~~~~~~~~~")

