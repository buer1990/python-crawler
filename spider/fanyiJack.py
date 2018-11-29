# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         fanyiJack
# Description:  
# Author:       buer1990
# Date:         2018/11/22
#-------------------------------------------------------------------------------
from urllib import request, parse
import json
if __name__ == '__main__':
    str='http://fanyi.youdao.com/translate'
    From_Data={}
    From_Data['i']='jack'
    From_Data['from']='AUTO'
    From_Data['to']='AUTO'
    From_Data['smartresult']='dict'
    From_Data['client']='fanyideskweb'
    From_Data['keyfrom']='fanyi.web'
    From_Data['action']='FY_BY_REALTIME'
    From_Data['version'] = '2.1'
    From_Data['doctype']='json'
    # From_Data['typoResult']='false'
    # From_Data['doctype'] = 'json'
    # From_Data['salt'] = '1542941168864'
    data=parse.urlencode(From_Data).encode('utf-8')
    res=request.urlopen(str,data)
    print(res.info())
    print(res.getcode())
    html=res.read().decode('utf-8')
    result=json.loads(html)
    translateResult=result['translateResult'][0][0]['tgt']
    print(translateResult)