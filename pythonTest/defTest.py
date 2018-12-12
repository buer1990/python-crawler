# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         defTest
# Description:  
# Author:       buer1990
# Date:         2018/12/11
#-------------------------------------------------------------------------------
def hello():
    print('hello world!\n\r\t')
    print('!!!!!!!!!!!!!!!!!!!!!!!!!\n\r\t')
hello()

def are(a,b):
    return a*b
print(are(1,2))
print('!!!!!!!!!!!!!!!!!!!!!!!!!\n\r')

def ptme(str):
    print(str)
    return
ptme("打印测试1")
ptme("打印测试2")

def changeInt(a):
    a=10
    print(a)
b=2
changeInt(b)
#结果不修改b值
print(b)

def changeList( list):
    list.append([0,0,0,0,])
    print("自定义函数:",list)
    return
mylist=[1,1,1,1,]
changeList(mylist)
#结果修改了mylist值
print(mylist)

def print元祖参数(arg1,*vartuple):
    "打印任何传入的参数"
    print(arg1,vartuple)
    for arg in vartuple:
        print(arg)
    return
print元祖参数(10)
print('~~~~~~~~~~~~~~~~~~~~~~`')
print元祖参数(10,11,12,13,)

def print字典参数(arg1,**vardict):
    print(arg1,vardict)
    for i,v in vardict.items():
        print({i:v})
    return
print字典参数(100,)
print('~~~~~~~~~~~~~~~~~~~~~~`')
print字典参数(100,a=101,b=102,c=10333,)


def f(a,b,*,d):
    return a+b+d
print(f(1,2,d=4))
print('~~~~~~~~~~~~~~~~~~~~~~`')


sum =lambda arg1,arg2:arg1+arg2
print(sum(1,2))
print('~~~~~~~~~~~~~~~~~~~~~~`')

