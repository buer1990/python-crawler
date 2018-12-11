# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         insertMysqlTest
# Description:  
# Author:       buer1990
# Date:         2018/12/10
#-------------------------------------------------------------------------------
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='python3sql'
)
sql='insert into sites (name,url) values (%s,%s)'
val=('python2mysql','http;//www.baidu.com')
print(mydb)
mycursor=mydb.cursor()
mycursor.execute(sql,val)
mydb.commit()    # 数据表内容有更新，必须使用到该语句
print(mycursor.rowcount, "记录插入成功。")
mycursor.execute('show tables')
for x in mycursor:
    print(x)

print("~~~~~~~~~~~~~~~~~~批量插入~~~~~~~~~~~~~~~~~")

val2=[('百度','www.baidu.com'),
      ('腾讯','http://tengxun.cn'),
      ('新浪','http://sina.com')]
mycursor.executemany(sql,val2)
mydb.commit()
print(mycursor.rowcount,"批量插入成功")