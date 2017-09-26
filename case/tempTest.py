# -*- coding: UTF-8 -*- 
from common.md5Base import md5Encode
import json
class test:
    def test1(self):
        md5Base1 = md5Encode()
        md5 = md5Base1.md5made("123456")
        print md5
        
        
if __name__ == '__main__':
    test22 = test()
    test22.test1()