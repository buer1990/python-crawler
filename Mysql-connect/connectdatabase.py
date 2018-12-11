# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         connectdatabase
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
print(mydb)
mycursor=mydb.cursor()
#mycursor.execute("CREATE TABLE sites (name VARCHAR(255), url VARCHAR(255))")
mycursor.execute("show tables")
for x in mycursor:
    print(x)
try:
    mycursor.execute("alter table sites add column id int auto_increment primary key ")
except Exception as e:
    print(e)