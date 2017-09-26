# -*- coding: UTF-8 -*- 
import os
class rootDirectory:
    '''    获取项目的根目录    '''
    def getRootDirectory(self):
        project_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
       
        return project_dir
        
