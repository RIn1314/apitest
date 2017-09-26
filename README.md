# apitest
接口测试框架

## case目录：
`demo目录`
- case\suite ：testSuites
- case ：test3，test4
> 直接运行testSuites，它将分别运行test3和test4。

## common目录：
封装公共方法。
- common\error：错误类（暂时没用）
- common\jsonBase：读取测试json数据
- common\loginBase：登录
- common\Md5Base：MD5加密
- common\resultBase：判断，验证测试结果，并将其输出到/result目录
- common\testBase： 引用 unittest，定义参数，作为测试基类
- common\timeBase：获取当前时间

## config目录：
- /config/rootDirectory :获取根目录


## data目录：
 - data1.json ：存放测试数据
 ```
 "testData1": {
        "Base_Host":  "http://127.0.0.1:8080/cdsxfsys",
        "headers": "user-agent:my-app/0.0.1",
        "url": "/contradiction/getWarnDepList" ,
        "payload1": "type=department",
        "loginUrl": "/login/in",
        "userName": "auhyjbzxx",
        "password": "e10adc3949ba59abbe56e057f20f883e"
    }
 ```
 
 ## logs目录：
- /logs :暂时没用

 ## result目录：
- /result/2017-xx月-xx日Report.html :打印测试报告（一天内多次测试，会覆盖上次的报告）





