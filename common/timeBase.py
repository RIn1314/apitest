#-- encoding:utf-8 -- 
import time
class timeBase: 
    def getNowTime(self): 
        '''
        获取当前时间
        time1 年月日时分秒
        time2 年月日
        '''
        time1 =  time.strftime('%Y-%m-%d %X',time.localtime())
        time2 =  time.strftime('%Y-%m-%d',time.localtime())
        return time2
 
