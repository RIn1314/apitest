# -*- coding: UTF-8 -*- 
import json
from config.rootDirectory import rootDirectory
class jsonBase:
    def readJson(self,fileName):
        getRootDirectory = rootDirectory()
        project_dir = getRootDirectory.getRootDirectory()
        jsonPath1 =  project_dir + "\\data\\"+ fileName
        with open(jsonPath1, 'r') as f:
            data = json.load(f)
            return data
            
