# -*- coding: UTF-8 -*- 
import json
class jsonBase:
    def readJson(self,fileName):
        jsonPath1 =  "E:\\Eclipse\\Workspace\\apiTest_xf2.0\\data\\"+ fileName
        with open(jsonPath1, 'r') as f:
            data = json.load(f)
            return data
            
