# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         selectTest
# Description:  
# Author:       buer1990
# Date:         2018/12/11
#-------------------------------------------------------------------------------
import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='root',
    database='python3sql'
)
sql='select *from sites where id=9 '
sql2="select *from sites where url like '%http%'"
sql3="select *from sites where url like %s"
sql4="select *from sites    order by name desc"
url=("%baidu%",)

mycursor=mydb.cursor()
mycursor.execute(sql4)
myresult=mycursor.fetchall()
for x in myresult:
    print(x)