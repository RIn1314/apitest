# -*- coding: utf-8 -*
import requests
from common.timeBase import timeBase
import HTMLTestRunnerCN
from config.rootDirectory import rootDirectory
class resultBase:
    '''    验证测试结果     '''
    def assertInfo(self,request,assertKeyword,showContent):
        '''    如果showContent为1，那么展示request的content信息    '''
        content =  request.text
        if showContent == 1:
            print content
        if (request.status_code == requests.codes.ok):
            print u"        状态码正确："+str(request.status_code)
        else:
            print u"        状态码错误："+str(request.status_code)
        try:           
            assert( assertKeyword in content)
            isPassed = 1
        except AssertionError:
            isPassed = 2
            print u"    Error : 关键词"+assertKeyword+u"未正确匹配！"
            '''    判断是否登录成功    '''
        try:
            assert (u"重新登录" in content)
            print u"    Error : "+u"登录错误！"
            isPassed = 0
        except AssertionError:

            pass

        return request,isPassed
    
    def TestInfo(self,request,isPassed):
        '''    判断测试结果信息  '''
        '''    isPassed： 0 不通过 ，1 通过，2  assert阶段错误    '''
        print "    URL : "+request.url
        if isPassed==1:
            print "    测试通过"
        elif isPassed==2:
            print "    测试未通过，原因：关键词未匹配"
        else:
            print "    测试未通过，原因：登录错误"
            
            
    def outputReport(self,suite):
        getTime = timeBase()
        timeNow = getTime.getNowTime()
        getRootDirectory = rootDirectory()
        path = getRootDirectory.getRootDirectory()
        filePath =path+ "\\result\\"+ timeNow +"Report.html"       #确定生成报告的路径 

        fp = file(filePath,'wb')
        runner = HTMLTestRunnerCN.HTMLTestRunner(
        stream=fp,
        title=u'自动化测试报告', 
        description='详细测试用例结果',    #不传默认为空
        tester=u"RIn"     #测试人员名字，不传默认为QA
        )
        #运行测试用例
        runner.run(suite)
        fp.close()


