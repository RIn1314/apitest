# -*- coding: utf-8 -*
import requests
from common.error import LoginError

class loginBase:
    '''
    登录
    '''
    
    def login(self,userName,password,loginUrl): 
        '''输入 姓名，密码，登录url'''
        
        headers = {'user-agent': 'my-app/0.0.1'}
        payload = (('userName', userName), ('userPwd', password),\
                   ('validateCode', '****'))


        session = requests.Session()
        try:
            session.post(loginUrl, params=payload,headers=headers)
        except LoginError,e:
            print e

        return session

