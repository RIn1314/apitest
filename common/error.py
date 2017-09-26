# -*- coding: utf-8 -*
import requests

class LoginError(AssertionError):
    '''
    错误信息
    '''
    def __init__(self, arg):
        self.args = u"Error：登录信息错误！"
   

