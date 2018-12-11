# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         connectTest
# Description:  
# Author:       buer1990
# Date:         2018/12/11
#-------------------------------------------------------------------------------
import pymysql

mydb=pymysql.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='python3sql'
)
sql='select *from sites'
mycursor=mydb.cursor()
mycursor.execute(sql)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)
mydb.close()