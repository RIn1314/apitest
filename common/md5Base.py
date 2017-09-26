# -*- coding: UTF-8 -*- 
__author__ = 'Rin'
import hashlib
'''
解析md5编码
    
'''
class md5Encode:
    def md5made(self, string1):
        m = hashlib.md5()
        m.update(string1)
        pws = m.hexdigest()
        return pws