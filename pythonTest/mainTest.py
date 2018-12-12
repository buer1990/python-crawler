# -*- coding: utf-8 -*-#

#-------------------------------------------------------------------------------
# Name:         mainTest
# Description:  
# Author:       buer1990
# Date:         2018/12/12
#-------------------------------------------------------------------------------

from pythonTest import deftest2

def test():
    print("本函数测试")
    print(__name__)

if __name__ == '__main__':
    test()
    dir(deftest2)
else:
    test()