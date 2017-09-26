# -*- coding: UTF-8 -*- 
__author__ = 'Rin'

import unittest

class testBase(unittest.TestCase):
    '''
    引用 unittest，定义参数，作为测试基类
    '''
    def setUp(self):
        print "********    测试开始    ********"
        
    
    def tearDown(self):
        print "    ********    测试结束    ********"
        
