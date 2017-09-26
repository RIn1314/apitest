# -*- coding: UTF-8 -*- 
from common.testBase import testBase
from common.resultBase import resultBase
from common.loginBase import loginBase
from common.jsonBase import jsonBase
class test4(testBase):    
    def testInfo4(self):
        """ Test method 查看admin的预警单位是否存在：四川省成都市委市政府信访局 """
        jsonBase1 = jsonBase()
        data = jsonBase1.readJson("data1.json")      
        Base_Host = data['testData1'][1]["Base_Host"]
        headers = {'user-agent': 'my-app/0.0.1'}
        # 获取预警单位list
        url = data['testData1'][1]["url"]  
        payload1 = data['testData1'][1]["payload1"]
         
        '''登录信息'''
        loginUrl = Base_Host+data['testData1'][1]["loginUrl"]
        userName = data['testData1'][1]["userName"]
        password =  data['testData1'][1]["password"]
        login = loginBase()  
        session= login.login(userName,password,loginUrl)
        
        '''本次request'''
        request = session.post(Base_Host+url, params=payload1,headers=headers)
        assertKeyword = u"四川省成都市委市政府信访局"
        '''
        模块：矛盾排查，
        功能：查看admin有没有正确的预警 四川省成都市委市政府信访局
        打印结果
        '''
        result = resultBase()
        request,isPassed = result.assertInfo(request, assertKeyword,0)        
        result.TestInfo(request,isPassed) 


