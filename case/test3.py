# -*- coding: UTF-8 -*- 
from common.testBase import testBase
from common.resultBase import resultBase
from common.loginBase import loginBase
from common.jsonBase import jsonBase

class test3(testBase):    
    def testInfo3(self):
        """ Test method 查看天府新区的预警单位是否存在：天府新区接待中心 """
        jsonBase1 = jsonBase()
        data = jsonBase1.readJson("data1.json")     
         
        Base_Host = data['testData1'][0]["Base_Host"]
        headers = {'user-agent': 'my-app/0.0.1'}
        # 获取预警单位list
        url = data['testData1'][0]["url"]  
        payload1 = data['testData1'][0]["payload1"]
         
        '''登录信息'''
        userName = data['testData1'][0]["userName"]
        password =  data['testData1'][0]["password"]
        loginUrl = Base_Host+data['testData1'][0]["loginUrl"]
        login = loginBase()  
        session= login.login(userName,password,loginUrl)
         
        '''本次request'''
        request = session.post(Base_Host+url, params=payload1,headers=headers)
        assertKeyword = u"四川省成都市天府新区群众接待中心"
        '''
        模块：矛盾排查，
        功能：查看天府新区街道有没有正确的预警和通知到天府接待中心
        打印结果
        '''
        result = resultBase()
        request,isPassed = result.assertInfo(request, assertKeyword,0)        
        result.TestInfo(request,isPassed)

