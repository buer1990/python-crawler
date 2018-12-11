# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         exceptTest
# Description:  
# Author:       buer1990
# Date:         2018/12/11
#-------------------------------------------------------------------------------
import pymysql

sql='insert into sites (name,url) values (%s,%s)'
val=('test','http;//www.baidu.com')

db=pymysql.connect('localhost','root','root','python3sql')
mycursor=db.cursor()
try:
    mycursor.execute(sql,val)
    db.commit()
except:
    db.rollback()

db.close()