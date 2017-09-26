# -*- coding: UTF-8 -*- 
import unittest
from case.test3 import test3
from case.test4 import test4
from common.resultBase import resultBase

def Suite1():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(test3("testInfo3"))
    print 'Suite1 运行'
    return suiteTest

def Suite2():
    suiteTest = unittest.TestSuite()
    suiteTest.addTest(test4("testInfo4"))
    print 'Suite2 运行'
    return suiteTest

def AllSuite():
    allTest = unittest.TestSuite((Suite1(),Suite2()))
    return allTest

#运行的时候，可以根据不同的要求，运行不同的Suite,或者全部运行，这样就方便管理每次运行的case
if __name__ == '__main__':
    resultBase = resultBase()
    resultBase.outputReport(AllSuite())

