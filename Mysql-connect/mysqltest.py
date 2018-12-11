# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         mysqltest
# Description:  
# Author:       buer1990
# Date:         2018/12/6
#-------------------------------------------------------------------------------
import mysql.connector

localdb=mysql.connector.connect(host='127.0.0.1',user='root',passwd='root')
print(localdb)
mycursor=localdb.cursor()
mycursor.execute("CREATE DATABASE python3sql")
mycursor.execute("show databases")
for x in mycursor:
    print(x)
